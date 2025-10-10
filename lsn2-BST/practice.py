from nodes import root, Node

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end = ',')
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=',')
    inOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=',')


def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif node.data > target:
        return search(node.right, target)
    else:
        return search(node.left, target)
    
def minValue(node):
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
        # node with one child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp
        # node with two children
        node.data = minValue(node.right).data
        node.right = delete(node.right, node.data)
    return node

def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node


node = insert(root, 11)
inOrderTraversal(root)

print('\n')
result = delete(root, 15)
inOrderTraversal(root)
