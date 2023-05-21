# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 523 ms
Beats | 98.79%
Memory | 17.2 MB
Beats | 16.69%
"""

""" 

"""

class Solution:
    def longestOnes(self, nums, k: int) -> int:
        n = len(nums)
        leftWindowPointer = 0
        for rightWindowPointer in range(n):
            
            k -= (1 - nums[rightWindowPointer])
            if k <  0:
                k += (1 - nums[leftWindowPointer])
                leftWindowPointer+=1
        return 1 + rightWindowPointer - leftWindowPointer
                     
    

sol = Solution()     
print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))