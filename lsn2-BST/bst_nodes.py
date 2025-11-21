class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        
def traverse_inOrder(node):
    if node is None:
        return []
    return (traverse_inOrder(node.left)
            +[node.key]
            +traverse_inOrder(node.right))

def find(node, key):
    if node is None:
        return None
    elif key == node.key:
        return node
    elif key < node.key:
        return find(node.left, key)
    elif key > node.key:
        return find(node.right, key)
    
def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
    elif key > node.key:
        node.right = insert(node.right, key, value)
    
    return node

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value
    else:
        return None
    
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

def display_keys(node, space='\t', level=0):
    # if node is empty
    if node is None:
        print(space*level + '0')
        return
    # if node is leaf node
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    # if the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1) 
    
def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]
    
    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    
    return root

def balance_bst(node):
    return make_balanced_bst(list_all(node))

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)