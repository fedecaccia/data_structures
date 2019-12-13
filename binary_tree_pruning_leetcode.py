# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Queue(object): # FIFO

    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return

        if self.is_prunable(root):
            root = None
            
        return root
            
    def is_prunable(self, node):
      
        if node is None:
            return True
        
        if self.is_prunable(node.left): node.left = None 
        if self.is_prunable(node.right): node.right = None 

        if node.left is None and node.right is None and node.val == 0:
            return True
        return False