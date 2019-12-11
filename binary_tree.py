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

        q = Queue()
        q.enqueue(start)

        while len(q)>0:

            start = q.dequeue()

            if start.left:
                q.enqueue(start.left)
            
            if start.right:
                q.enqueue(start.right)

            traversal += str(start.value) + " - "           

        return traversal

    def reverse_levelorder_print(self, start, traversal):

        q = Queue()
        q.enqueue(start)
        s = Stack()

        while len(q) > 0:

            n = q.dequeue()
            s.push(n)

            if n.right:
                q.enqueue(n.right)

            if n.left:
                q.enqueue(n.left)

        while not s.is_empty():
            traversal += str(s.pop().value) + " - "

        return traversal

    def height(self, node):

        if node is None:
            return 1

        q = Queue()
        l = Queue()
        
        q.enqueue(node)
        l.enqueue(1)

        higher_level = 1 # or 0 if last level has level 0

        while len(q)>0:

            node = q.dequeue()
            level = l.dequeue()
            
            if(level>higher_level):
                higher_level = level
            
            if node.left:
                q.enqueue(node.left)
                l.enqueue(level+1)
            
            if node.right:
                q.enqueue(node.right)
                l.enqueue(level+1)

        return higher_level

    def height_recursive(self, node):

        if node is None:
            return 0 # or -1 if last level has level 0

        left = self.height_recursive(node.left)
        right = self.height_recursive(node.right)

        if left > right:
            h = 1 + left
        else:
            h = 1 + right
        return h

    def size(self):
        """ Calculate number of nodes in the tree"""

        size = 0
        if self.root is None:
            return size

        q = Queue()
        q.enqueue(self.root)

        while len(q) > 0:

            n = q.dequeue()
            size += 1

            if n.left:
                q.enqueue(n.left)

            if n.right:
                q.enqueue(n.right)

        return size

    def size_recursive(self, node):
        """ Calculate number of nodes in the subtree"""

        if node is None:
            return 0

        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)

        
