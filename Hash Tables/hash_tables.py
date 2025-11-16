MAX_HASH_TABLE = 4089

class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE):
        self.data_list = [None] * max_size
        
    def insert(self, key, value):
        idx = BasicHashTable.get_index(self.data_list, key)
        self.data_list[idx] = key, value
    
    def find(self, key):
        idx = BasicHashTable.get_index(self.data_list, key)
        kv = self.data_list[idx]
        
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    def update(self, key, value):
        idx = BasicHashTable.get_index(self.data_list, key)
        
        self.data_list[idx] = key, value
        
    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]
    
    @staticmethod
    def get_index(data_list, a_string):
        result = 0
        for char in a_string:
            a_number = ord(char)
            result += a_number
        return result % len(data_list)
