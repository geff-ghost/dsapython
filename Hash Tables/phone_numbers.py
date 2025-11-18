from hash_tables import BasicHashTable

phone_numbers = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    'Listen' : '001-2342',
    "Charlie": "555-8765",
    "Diana": "555-4321",
    'Aakash': '555-0001',
    'Siddhanth': '555-0002',
    'Silent' : '456-2245',
    
}


basic_table = BasicHashTable()

for key, value in phone_numbers.items():
    basic_table.insert(key, value)
    
alice = basic_table.find('Alice')
print(f'Alice tell: {alice}')
    
basic_table.update('Bob', '455-3456')
bob = basic_table.find('Bob')
print(f'Bob: {bob}')

keys = basic_table.list_all()
print(keys)