
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.key, end=',')
    inOrderTraversal(node.right)

def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)

    # if the node is empty
    if node is None:
        print(space*level + 'None')
        return
    # if the node is a leaf
    if node.left  is None and node.right is None:
        print(space*level + str(node.key))
        return
    # if the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)

# write a function to convert the tree back to a tuple
def tree_to_tuple(data):
    ...

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node



tuple = parse_tuple(((1,3,None),2,((None,3,4),5,(6,7,8))))

# inOrderTraversal(tuple)
display_keys(tuple,'  ')

in_order = traverse_in_order(tuple)
print(in_order)
