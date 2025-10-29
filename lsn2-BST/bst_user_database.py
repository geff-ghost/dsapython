from bst_user_profile import jadhesh, biraj, sonaksh

class BSTNode:
    def __init__(key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def display_keys(self, node, space='\t', level=0):
        # if node is empty
        if node is None:
            print(space * level + '∅')
            return
        # if node is a leaf
        if node.left is None and node.right is None:
            print(space * level + str(node.key))
            return
        # if node has children
        TreeNode.display_keys(node.right, space, level + 1)
        print(space * level + str(node.key))
        TreeNode.display_keys(node.left, space, level + 1)

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = BSTNode(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node

    return node

tree = insert(jadhesh, biraj.username, biraj)

root = BSTNode(jadhesh.username, jadhesh)

root.display_keys(tree)
            