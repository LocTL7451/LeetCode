# 1929. Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/description/

""" 
Runtime | 101 ms
Beats | 25.63%
Memory | 16.7 MB
Beats | 26.96%
"""

""" 
    We just add one array to another 
"""

class Solution:
    def getConcatenation(self, nums):
        return nums + nums
    
sol = Solution()
print(sol.getConcatenation("capiTalIze tHe titLe"))