
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left: 'TreeNode | None' = None
        self.right: 'TreeNode | None' = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=' ')
    inOrderTraversal(node.right)


def search(node, target):
    if node is None:
        return None
    if node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)
    
def insert(node, data):
    if node is None:
        return TreeNode(data)
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, data):
    if node is None:
        return node
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)
    return node

# Create nodes
root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

# Build the complete tree structure
root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18  # Connect node18 as left child of node19

# Traverse
# print("In-order traversal:")
# inOrderTraversal(root)

# Search
# search_result = search(root, 9)
# print("\nSearch result for 8:", search_result.data if search_result else "Not found")

# Inserting a node
insert(root, 9)
print("In-order traversal after inserting 56:")
inOrderTraversal(root)

# Finding minimum value node
# minValueNode_result = minValueNode(root)
# print("\nMinimum value node:", minValueNode_result.data if minValueNode_result else "Tree is empty")

# delete(root, 14)
# print("In-order traversal after deleting:")
# inOrderTraversal(root)
