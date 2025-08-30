import csv


class Item:
    pay_rate = 0.8 # a class attribute
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        # asigning to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Adding instances to the class Attribute all
        Item.all.append(self) # adds all the instances to the list once created

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def appy_discount(self):
        self.price = self.price * Item.pay_rate

    @classmethod
    def instanciate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name= str(item['name']),
                price= float(item['price']),
                quantity= int(item['quantity']),
            )

    @staticmethod
    def is_integer(num):
        #this function returns True if an int or false if not

        if isinstance(num, float):
            #returns True or False, but count's out zeros ie 10.0 -> 10
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

    def okay_phones(self):
        pass

phone1 = Phone('jscPhonev10', 500, 5, 1)
phone2 = Phone('jscPhonnev20', 700, 5, 1)

Item.instanciate_from_csv()
print(Item.all)