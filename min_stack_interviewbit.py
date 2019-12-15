class MinStack:
    
    def __init__(self):
        self.elems = []
        self.min = [-1]
        
    # @param x, an integer
    def push(self, x):
        if self.min[-1]==-1:
            self.min.append(x)
        elif x<=self.min[-1]:
            self.min.append(x)
            
        self.elems.append(x)


    # @return nothing
    def pop(self):
        if len(self.elems)>0:
            if self.min[-1] == self.elems[-1]:
                self.min.pop()
            
            return self.elems.pop()

    # @return an integer
    def top(self):
        if len(self.elems)==0:
            return -1
        
        return self.elems[-1]


    # @return an integer
    def getMin(self):
        return self.min[-1]
