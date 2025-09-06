import time as t
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

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

def display_keys(node, space= '\t', level= 0):
    # print(node.key if node else None, level)

    # if the node is empty
    if node is None:
        print(space * level + 'None')
        return
    
    # if the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return
    
    # if the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)

# traverses the tree in an in-order manner
def traverse_in_order(node):
    if node is None:
        return []
    
    return (traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

# returns the the lenght from the root node to the leaf node
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

# returns the number of nodes in the tree
def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


tree = parse_tuple(tree_tuple)

display_keys(tree)


# height = traverse_in_order(tree)
# print(height)

height= tree_height(tree)

print(height)

size = tree_size(tree)
print(size)