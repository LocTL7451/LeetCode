# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/
""" 
Runtime | 71 ms
Beats | 59.76%
Memory | 17.7 MB
Beats | 10.80%
"""

""" 
    The approach here is to keep track of the index position of every number in the array as we traverse it
    We know that: 
        Target = Rem + N
        For every number Rem, we know that Rem = Target - N
    Using this information, we can calculate the remainder for every N in our nums array 
    For each N, we calculate Rem and check the hash map to see if we have found the position for that number or not 
"""

class Solution:
    def twoSum(self, nums, target: int):    
        sumDict = {}
        for i, j in enumerate(nums):
            rem = target - j
            if rem in sumDict:
                return [sumDict[rem], i]
            else:
                sumDict[j] = i

sol = Solution()     
print(sol.twoSum([2,7,11,15], 9))