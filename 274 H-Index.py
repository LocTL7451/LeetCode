# 274. H-Index
# https://leetcode.com/problems/h-index/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 47 ms
Beats | 51.90%
Memory | 16.6 MB
Beats | 21.16%
"""

"""
    My approach for this problem was to break up the problem into parts, starting by sorting the citations into ascending order. 
    From here, we can enumerate the array to pair each value with it's index.
    By comparing the value and index, we have a smarter way to determine the h index 
"""
class Solution:
    def hIndex(self, citations):
        
        citations = sorted(citations, reverse=True)
        retArray = []
        for i,v in enumerate(citations):
            print((i,v))
            if i < v: 
                retArray.append(1)
        return sum(retArray)
                
        

            
sol = Solution()
print(sol.hIndex([3,0,6,1,5]))
                
            
        
    
