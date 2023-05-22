# 1493. Longest Subarray of 1's After Deleting One Element
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 372 ms
Beats | 66.76%
Memory | 19.2 MB
Beats | 6.7%
"""

""" 
    The approach for this question is very similar to problem 1004, so I have included an exerpt from the documentation I wrote for 1004:
        The approach here is similar to problem 1456, in which we keep track of the number of 0's in the current window subarray by 
        incrementing and decrementing k. K gives us indications of how many 0's exist, where the case of k < 0 suggests there are too many
         0's in the current window.
    
         We then initialise a left and right window pointer, where the right pointer always moves to the right every iteration, and the left 
        only moves when the current window subarray contains too many 0's.  
    The only alterations we make here are changing the number of allowed 0's from variable to a constant 1. 
    Due to the requirement of always having to delete 1 element being present, we also alter the return statement to not add 1 to the difference in
    pointer positions.
    
"""

class Solution:
    def longestSubarray(self, nums) -> int:
        n = len(nums)
        k = 1
        leftWindowPointer = 0
        if n == 1 and nums[0] == 0:
            return 0

        for rightWindowPointer in range(n):
            
            k -= (1 - nums[rightWindowPointer])
            if k <  0:
                k += (1 - nums[leftWindowPointer])
                leftWindowPointer+=1
        return rightWindowPointer - leftWindowPointer
                     
    

sol = Solution()     
print(sol.longestSubarray([1,1,0,1]))