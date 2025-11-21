from bst_nodes import *
class TreeMap:
    def __init__(self):
        self.root = None
    
    # combination of both insert and update
    def __setitem__(self, key, value):
        node = find(self.root, key)
        # if node is not found
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)
    
    # this is the find operation
    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None
    
    # returns a list of all the users
    def __iter__(self):
        return (x for x in list_all(self.root))
    
    # returns the size of the binary tree
    def __len__(self):
        return tree_size(self.root)
    
    # display all the keys
    def display(self):
        return display_keys(self.root)