
class TreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) 
                + [self.key] 
                + TreeNode.traverse_in_order(self.right))

    def display_keys(self, space='\t', level=0):
        # if node is empty
        if self is None:
            print(space * level + '∅')
            return
        # if node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return
        # if node has children
        TreeNode.display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        TreeNode.display_keys(self.left, space, level + 1)

    # write a function to convert the tree back to a tuple
    def tree_to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return (TreeNode.tree_to_tuple(self.left), self.key, TreeNode.tree_to_tuple(self.right))

    def __str__(self):
        return "Binary Tree <{}>".format(self.tree_to_tuple())
    
    def __repr__(self):
        return "Binary Tree <{}>".format(self.tree_to_tuple())
    
    @staticmethod
    def parse_tuple(data):
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return node




# tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

# tree = TreeNode.parse_tuple(tree_tuple)
# print(tree)
# print("Height:", tree.height())
# print("Size:", tree.size())
# print("In-order Traversal:", tree.traverse_in_order())
# tree.display_keys('  ')

# print("Tree to Tuple:", tree.tree_to_tuple())

