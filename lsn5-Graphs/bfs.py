
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertNode(self, data):
        if not self.root:
            self.root = Node(data)
            return self.root
        else:
            # recurse the rest of the nodes to insert at the right position
            self._insert_recursive(self.root, data)
        return self.root

    def _insert_recursive(self, curr, value):
        if value <= curr.data:
            if curr.left is None:
                curr.left = Node(value)
            else:
                self._insert_recursive(curr.left, value)
        elif value > curr.data:
            if curr.right is None:
                curr.right = Node(value)
            else:
                self._insert_recursive(curr.right, value)

    def bfs(self):
        """
        Breath-First Search (Level Order Traversal) using a Queue.
        Visits all the nodes at a given level before moving to the next level
        """
        if not self.root:
            return []
        queue = [self.root]
        result = []

        while queue:
            # pop the first element in the queue
            curr = queue.pop(0)
            result.append(curr.data)
            # checking whether the current element has both left and right child nodes and adding them to the queue
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        return result

    def dfs(self):
        if not self.root:
            return []
        stack = [self.root]
        result = []

        while stack:
            # pop() removes the last element that was added
            curr = stack.pop()
            result.append(curr.data)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return result


    def _OrderedTraversal(self, node):
        if node is None:
            return []
        return (
            self._OrderedTraversal(node.left) +
            [node.data] +
            self._OrderedTraversal(node.right)
        )

    def inOrderTraversal(self):
        if not self.root:
            return []
        return self._OrderedTraversal(self.root)
            


arr = [7, 3, 8, 5, 9, 2]
tree = BinaryTree()
for val in arr:
    root = tree.insertNode(val)

print(f"InOrderTraversal: {tree.inOrderTraversal()}")
print('')

print(f"Breath-First Search(queue): {tree.bfs()}")
print('')

print(f'Depth-First Search(stack): {tree.dfs()}')

