
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(13)
node7 = Node(7)
node15 = Node(15)
node3 = Node(3)
node8 = Node(8)
node14 = Node(14)
node19 = Node(19)
node18 = Node(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18
