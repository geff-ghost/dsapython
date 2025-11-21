MAX_HASH_TABLE = 4089

class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE):
        # create a list of size 'max_size'
        self.data_list = [None] * max_size
    
    def insert(self, key, value):
        # find the index of the key using get_index
        idx = BasicHashTable.get_valid_index(self.data_list, key)
        # store the key-value pair at the right index
        self.data_list[idx] = key, value
    
    def find(self, key):
        # find the index for the key usinf get_index
        idx = BasicHashTable.get_valid_index(self.data_list, key)
        # retrieve the value data stored at the index
        kv = self.data_list[idx]
        
        # return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    def update(self, key, value):
        # find the idx for the key using get_index
        idx = BasicHashTable.get_valid_index(self.data_list, key)
        
        self.data_list[idx] = key, value
        
    def list_all(self):
        # store the new key-value pair at the right index
        return [kv[0] for kv in self.data_list if kv is not None]
    
    @staticmethod
    def get_index(data_list, a_string):
        result = 0
        for char in a_string:
            a_number = ord(char)
            result += a_number
        return result % len(data_list)

    @staticmethod
    def get_valid_index(data_list, key):
        # Start with the index returned by get_index
        idx = BasicHashTable.get_index(data_list, key)
        
        while True:
            # Get the key-value pair stored at idx
            kv = data_list[idx]
            
            # If it is None, return the index
            if kv is None:
                return idx
            
            # if the stored key matches the given key, return the index
            k, v = kv
            if k == key:
                return idx
            
            # Move to the next index
            idx += 1
            
            # Go back to the start if you have reached the end of the array
            if idx == len(data_list):
                idx = 0
    
    
# data_list2 = [None] * MAX_HASH_TABLE

# print(get_valid_index(data_list2, 'listen'))
# print(get_valid_index(data_list2, 'silent'))

# data_list2[get_valid_index(data_list2, 'listen')] = ('listen', 999)
# print(get_valid_index(data_list2, 'silent'))


