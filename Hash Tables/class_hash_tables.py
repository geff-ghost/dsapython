MAX_HASH_TABLE = 4096

class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE):
        self.data_list = [None] * max_size
        
    def get_valid_index(self, key):
        # use Python in-built 'hash' function and implement lenear probinging
        idx = hash(key) % len(self.data_list)
        
        while True:
            # get the key-value pair stored at the idx
            kv = self.data_list[idx]
            
            # if it is None return the index
            if kv is None:
                return idx
            
            # if the stored key matches the given key, return idx
            k, v = kv
            if k == key:
                return idx
            
            # move to the next index
            idx += 1
            
            # go back to the start if you have reached the end of the array
            if idx == len(self.data_list):
                idx = 0
            
    
    def __getitem__(self, key):
        # find the index for the key using get_valid_index
        idx = self.get_valid_index(key)
        
        # retreive the data stored at the index
        kv = self.data_list[idx]
        
        # return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    def __setitem__(self, key, value):
        # the logic for 'insert/update' is implemented here
        # find the idx for the key using get_index
        idx = self.get_valid_index(key)
        
        # store the new key-value pair at the right index
        self.data_list[idx] = key, value
    
    def __iter__(self):
        return (x for x in self.data_list if x is not None)
    
    def __len__(self):
        return len([x for x in self])
    
    def __repr__(self):
        key, value, ch = [kv for kv in self.data_list if kv is not None]
        return 'User: {}---> Tell: {} ---{}'.format(key, value, ch)
        
        
    def __str__(self):
        return repr(self)
    
tree = HashTable()
tree['Aaron'] = '999-3453'
tree['Jack'] = '783-2234'
tree['Miraa'] = '923-9830'

print(tree['Jay'])

print('')

print(list(tree))

print('')
print(tree)