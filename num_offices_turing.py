class Node(object):
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col

class Queue(object):

    def __init__(self):
        self.elems = []
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, node):
        self.elems.insert(0, node)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.elems.pop()


class Solution(object):
    def numOffices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # your code here

        grid = [[int(grid[r][c]) for c in range(len(grid[0]))] for r in range(len(grid))]

        max_row = len(grid)-1
        max_col = len(grid[0])-1

        belong_to_office = []
        for r in range(max_row+1):
            belong_to_office.append([])
            for c in range(max_col+1):
                belong_to_office[r].append(False)             

        num_offices = 0
        q = Queue()

        for r in range(max_row+1):        
            for c in range(max_col+1):

                # print(r,c,belong_to_office[r][c])

                if grid[r][c] == 1 and belong_to_office[r][c] == False:
                    num_offices += 1                    
                    n = Node(grid[r][c], r, c)
                    q.enqueue(n)
        
                while len(q)>0:

                    n = q.dequeue()
                    row = n.row
                    col = n.col
                    
                    if belong_to_office[row][col] == False:
                        belong_to_office[row][col] = True
                        
                        if row>0:
                            if grid[row-1][col] == 1 and belong_to_office[row-1][col] == False:
                                nb = Node(grid[row-1][col], row-1, col)
                                q.enqueue(nb)

                        if row<max_row:
                            if grid[row+1][col] == 1 and belong_to_office[row+1][col] == False:
                                nb = Node(grid[row+1][col], row+1, col)
                                q.enqueue(nb)

                        if col>0:
                            if grid[row][col-1] == 1 and belong_to_office[row][col-1] == False:
                                nr = Node(grid[row][col-1], row, col-1)
                                q.enqueue(nr)
                                
                        if col<max_col:
                            if grid[row][col+1] == 1 and belong_to_office[row][col+1] == False:
                                nr = Node(grid[row][col+1], row, col+1)
                                q.enqueue(nr)

        return num_offices

sol = Solution()
# matrix = [
#     [1,1,1,1,0],
#     [1,1,0,1,0],
#     [1,1,0,0,0],
#     [0,0,0,0,0]
# ]
# matrix = [
#     [1,1,0,0,0],
#     [1,1,0,0,0],
#     [0,0,1,0,0],
#     [0,0,0,1,1]
# ]
# matrix = [
#     [1,1,1,1,1],
#     [1,0,0,0,1],
#     [1,0,0,0,0],
#     [1,1,1,0,1]
# ]
# matrix = [
#     ['1','0','0','0','1'],
#     ['0','0','0','0','0'],
#     ['0','0','0','0','0'],
#     ['0','0','0','0','1']
# ]
matrix = [
    ['1','0','0','0','1'],
    ['0','0','1','0','0'],
    ['0','1','1','0','0'],
    ['0','0','0','0','1']
]
offices = sol.numOffices(matrix)
print(offices)