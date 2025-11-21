from class_hash_tables import HashTable

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

if __name__ == '__main__':
    basic_table = HashTable()

    # inserting key-value pairs
    for key, value in phone_numbers.items():
        basic_table[key] = value
        
    # finding a value from the hash table
    alice = basic_table['Alice']
    print(f'Alice tell: {alice}')
        
    # updating a value
    basic_table['Bob'] = '455-3456'
    bob = basic_table['Bob']
    print(f'Bob: {bob}')

    print('')
    print(list(basic_table))
    
    print('')
    print(len(basic_table))