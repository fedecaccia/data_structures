class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    
    def threeSumClosest(self, A, B):
        
        closest_sum = A[0] + A[1] + A[2]
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                for k in range(j+1, len(A)):
                    sum = A[i] + A[j] + A[k]
                    if abs(B-sum) < abs(B-closest_sum):
                        closest_sum = sum
                        
        return closest_sum

s = Solution()

assert(s.threeSumClosest([1,2,3,4], 3) == 6)
assert(s.threeSumClosest([1,2,1,4], 3) == 4)
assert(s.threeSumClosest([1,2,3,4,1,1,5,-1], 3) == 3)