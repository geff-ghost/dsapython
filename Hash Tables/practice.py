MAX_HASH_TABLE = 4098
from jovian.pythondsa import evaluate_test_case


def get_index(data_list, key):
    result = 0

    for char in key:
        num = ord(char)
        result += num

    list_index = result % len(data_list)
    return list_index



class Basic_Hash_Table:
    def __init__(self, max_size=MAX_HASH_TABLE):
        self.data_list = [None] * max_size

    def insert(self, key, value):
        idx = get_index(self.data_list, key)
        self.data_list[idx] = (key, value)

    def find(self, key):
        idx = get_index(self.data_list, key)

        kv = self.data_list[idx]

        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        idx = get_index(self.data_list, key)
        self.data_list[idx] = key, value

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]


phone_numbers = {
    'Odhiambo': '152-3122',
    'Aakash': '901-3958',
    'Siddhant': '456-2246',
    'Hemanth': '257-2945'
}

basic_table = Basic_Hash_Table()
for key, value in phone_numbers.items():
    basic_table.insert(key, value)


users = basic_table.list_all()
print(users)
print('')

print('Aakash: ',basic_table.find('Aakash'))

weight = 0
lr = 0.01

for i in range(100):
    pred = weight * 2
    loss = (pred - 4) ** 2
    grad = 2 * 2 * (pred - 4)
    weight -= lr * grad

print('Final weight: ', weight) 