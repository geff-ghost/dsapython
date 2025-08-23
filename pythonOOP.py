


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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

class Phone(Item):
    def __init__(self, name, price, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

class Laptop(Item):
    def __init__(self, name, price, brand,quantity=0):
        super().__init__(name, price, quantity)
        self.brand = brand

item = Item('Tablet', 1000, 2)
phone = Phone('Android', 1000, 3, 1)
laptop = Laptop('Jarvis', 500, 'HP', 2)


print(item.all)
print(phone.all)
print(laptop.all)
