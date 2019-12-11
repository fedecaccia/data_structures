class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Stack(object): # LIFO

    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  # release last item
        if not self.is_empty():
            return self.items.pop()

    def peek(self): # show last item
        if not self.is_empty():
            return self.items[-1].value

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s


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

class BinaryTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        
        # Recursive DFS raversals
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")

        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")

        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")

        # Queue-Stacks BFS traversals
        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root, "")

        elif traversal_type == "reverse levelorder":
            return self.reverse_levelorder_print(self.root, "")

        else:
            print("Traversal type " + str(traversal_type) + " not recognized.")
            return False

    def preorder_print(self, start, traversal):
        """Root-> Left -> Right"""

        if start is not None:
            traversal += str(start.value) + " - "
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)            

        return traversal        
    
    def inorder_print(self, start, traversal):
        """Left -> Root-> Right"""

        if start is not None:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + " - "
            traversal = self.inorder_print(start.right, traversal) 

        return traversal        
    
    def postorder_print(self, start, traversal):
        """Left -> Right -> Root"""

        if start is not None:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal) 
            traversal += str(start.value) + " - "

        return traversal 

    def levelorder_print(self, start, traversal):

        return traversal

    def reverse_levelorder_print(self, start, traversal):

        return traversal

    
