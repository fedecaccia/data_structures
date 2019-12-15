class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):

        self.capacity = capacity
        self.size = 0

        self.start = None
        self.end = None

        self.nodes = {}
        self.keys = set()

    def putNodeFirst(self, node):

        if node is self.start:
            return

        if self.last == node and node.prev is not None:
            self.last = node.prev
                
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None and node:
            node.next.prev = node.prev

        node.prev = None
        node.next = self.start
        self.start.prev = node
        self.start = node

    # @return an integer
    def get(self, key):

        if key in self.keys:

            self.putNodeFirst(self.nodes[key])            

            return self.start.value
        
        return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):

        if key in self.keys:
            self.nodes[key].value = value
            self.putNodeFirst(self.nodes[key])

        else:
            n = Node(key, value)

            if self.start is not None:
                self.start.prev = n
                n.next = self.start

            self.start = n
            self.nodes[key] = n
            self.keys.add(key)

            if self.size == 0:
                # print("Setting last: ", n.key)
                self.last = n

            if self.size < self.capacity:
                self.size += 1

            else:
                
                lkey = self.last.key
                
                if self.last is not None:
                    self.last = self.last.prev
                                
                self.nodes[lkey].prev.next = None
                del self.nodes[lkey]
                self.keys.remove(lkey)

    def printKeys(self):
        nptr = self.start
        l = []
        while nptr is not None:
            l.append(nptr.key)
            nptr = nptr.next


print("lru = LRUCache(2)")
lru = LRUCache(2)

print("lru.set(1,10)")
lru.set(1,10)
lru.printKeys()

print("lru.set(5,12)")
lru.set(5,12)
lru.printKeys()

print("assert(lru.get(1) == 10)")
assert(lru.get(1) == 10)
lru.printKeys()

print("assert(lru.get(5) == 12)")
assert(lru.get(5) == 12)
lru.printKeys()

print("assert(lru.get(10) == -1)")
assert(lru.get(10) == -1)
lru.printKeys()

print("lru.set(6,14)")
lru.set(6,14)
lru.printKeys()

print("assert(lru.get(1) == -1)")
assert(lru.get(1) == -1)
lru.printKeys()

print("test lru idea")

print("assert(lru.get(5) == 12)")
assert(lru.get(5) == 12)
lru.printKeys()

print("lru.set(32,32)")
lru.set(32,32)
lru.printKeys()

print("assert(lru.get(6) == -1)")
assert(lru.get(6) == -1)
lru.printKeys()

print("assert(lru.get(32) == 32)")
assert(lru.get(32) == 32)
lru.printKeys()

print("assert(lru.get(5) == 12)")
assert(lru.get(5) == 12)
lru.printKeys()

print("lru.set(5,5)")
lru.set(5,5)
lru.printKeys()

print("assert(lru.get(5) == 5)")
assert(lru.get(5) == 5)
lru.printKeys()

print("assert(lru.get(32) == 32)")
assert(lru.get(32) == 32)
lru.printKeys()

print("lru.set(6,6)")
lru.set(6,6)
lru.printKeys()

print('assert(lru.get(5) == -1)')
assert(lru.get(5) == -1)
lru.printKeys()