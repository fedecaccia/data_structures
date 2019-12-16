class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        if len(ratings) == 0:
            return 0
        
        candies = [0]*len(ratings)
        
        prev_val = ratings[0]
        candies[0] = 1
        
        for i in range(1,len(ratings)):
            
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
                
            elif ratings[i] == ratings[i-1]:
                candies[i] = 1
                
            elif ratings[i] < ratings[i-1] and candies[i-1] > 1:
                candies[i] = 1
                
            else:
                candies[i] = 1
                j = i-1
                while ratings[j] > ratings[j+1] and candies[j] <= candies[j+1]:
                    candies[j] = candies[j+1] + 1
                    j = j-1
                
        return sum(candies)


s = Solution()
assert(s.candy([]) == 0)
assert(s.candy([5]) == 1)
assert(s.candy([1,0,2]) == 5)
assert(s.candy([1,2,2]) == 4)
assert(s.candy([1,2,3,4,3,2,1]) == 16)
assert(s.candy([1,2,3,4,2,2,1]) == 14)