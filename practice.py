

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left: 'TreeNode | None' = None
        self.right: 'TreeNode | None' = None

# preOrderTraversal of the tree
def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=', ')
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

# inOrderTraversal of the Tree
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=', ')
    inOrderTraversal(node.right)

# postOrderTraversal of the Tree
def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=', ')

def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

def insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, data):
    if not node:
        return None
    
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # Node with only one child or no child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp
        
        # Node with two children, get the in-order successor
        node.data = minValueNode(node.right).data
        node.right = delete(node.right, node.data)

    return node

# creating the nodes
root = TreeNode(13)
node7 = TreeNode(7)
node3 = TreeNode(3)
node8 = TreeNode(8)
node15 = TreeNode(15)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)


# Creating the Binary Tree
root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Searching for a node
# search_result = search(root, 0)
# print("\nSearch result:", search_result.data if search_result else "Not found") #tenary operator

# Inserting a value
# insert(root, 9)
# print("In-order traversal after inserting 9:")
# inOrderTraversal(root)

# finding the minValueNode in the tree
# minValueNode_result = minValueNode(root)
# print("\nMinimum value node:", minValueNode_result.data if minValueNode_result else "Tree is empty")

# Deleting a node
delete(root, 14)
print("In-order traversal after deleting 14:")
inOrderTraversal(root)
