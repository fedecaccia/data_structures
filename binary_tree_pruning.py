from binary_tree import BinaryTree


class BinaryTreePruning(BinaryTree):

    def __init__(self, root_value):
        if root_value not in [0,1]:
            raise ValueError("Only 0 or 1 values are accepted")

        super().__init__(root_value)

    def is_prunable(self, node):
      
        if node is None:
            return True
        
        if self.is_prunable(node.left): node.left = None 
        if self.is_prunable(node.right): node.right = None 

        if node.left is None and node.right is None and node.value == 0:
            return True
        return False

    def prune(self):

        if self.root is None:
            return

        if self.is_prunable(self.root):
            self.root = None