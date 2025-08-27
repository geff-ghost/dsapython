

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


# creating the nodes
root = TreeNode('R')
nodeA = TreeNode('A')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeB = TreeNode('B')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')


# Creating the Binary Tree
root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print('\npreOrderTraversal of the Tree')
preOrderTraversal(root)

print('')

print('\ninOrderTraversal of the Tree')
inOrderTraversal(root)

print('')

print('\npostOrderTraversal of the Tree')
postOrderTraversal(root)