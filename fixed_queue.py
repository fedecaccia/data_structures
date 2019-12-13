class FixedQueue(object):

    def __init__(self, size):

        self.size = size
        self.used = 0
        self.elems = [None]*size

    def __len__(self):

        return self.used

    def getElems(self):

        return self.elems

    def enqueue(self, value):

        if self.used >= self.size:
            raise Exception("No space to add a new element")

        self.elems[self.used] = value
        self.used += 1

    def dequeue(self):

        if self.used == 0:
            raise IndexError("Trying to dequeue an empty list")

        returned_value = self.elems[0]
        for i in range(self.used-1):
            self.elems[i] = self.elems[i+1]

        self.used -= 1

        return returned_value

class Node(object):

    def __init__(self, value):

        self.value = value
        self.next = None

class FixedQueueLinkedList (object):

    def __init__(self, size):

        self.size = size
        self.used = 0
        self.first_elem = None
        self.last_elem = None

    def __len__(self):

        return self.used

    def enqueue(self, value):

        if self.used >= self.size:
            raise Exception("No space to add a new element")
        
        self.used += 1
        n = Node(value)

        if self.last_elem is None:
            self.first_elem = n
            self.last_elem = n
        else:
            self.last_elem.next = n
            self.last_elem = n


    def dequeue(self):

        if self.used == 0:
            raise IndexError("Trying to dequeue an empty list")

        returned_value = self.first_elem.value
        self.used -= 1
        
        self.first_elem = self.first_elem.next

        return returned_value