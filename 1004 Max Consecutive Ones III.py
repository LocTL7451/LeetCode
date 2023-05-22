# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 523 ms
Beats | 98.79%
Memory | 17.2 MB
Beats | 16.69%
"""

""" 
    The approach here is similar to problem 1456, in which we keep track of the number of 0's in the current window subarray by 
    incrementing and decrementing k. K gives us indications of how many 0's exist, where the case of k < 0 suggests there are too many
    0's in the current window.
    
    We then initialise a left and right window pointer, where the right pointer always moves to the right every iteration, and the left 
    only moves when the current window subarray contains too many 0's.
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