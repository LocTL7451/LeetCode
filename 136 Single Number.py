# 136. Single Number
# https://leetcode.com/problems/single-number/description/

""" 
Runtime | 135 ms
Beats | 73.93%
Memory | 19.2 MB
Beats | 11.62%
"""

""" 
    The approach here is to use the reduce method from functools to loop through the nums array and reduce each position to the resulting 
    XOR output
"""
from functools import reduce
from operator import xor
class Solution:
    def singleNumber(self, nums) -> int:
        return reduce(xor,nums)
            

sol = Solution()     
print(sol.singleNumber([4,1,2,1,2]))

