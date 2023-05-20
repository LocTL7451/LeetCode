# 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&id=leetcode-75
""" 
Runtime | 1077 ms
Beats | 56.72%
Memory | 32.5 MB
Beat | 13.32%
"""

""" 
    The approach here is just to focus on getting a correct value for k. We start by setting i and j to infinity, then looping
    through the array. If the current value is greater than the current j value, this implies that i is valid and j is valid, so
    current value being larger than j suggests that current value is a valid fit for k, so we return True.
    We also check if the current value is less than i, setting the i value to current value. 
    Otherwise, we just set the second value to current value as current value will always be less than infinity.
    If we loop all the way through and don't find a valid position for k, we return False
"""
import math as m
class Solution:
    def increasingTriplet(self, nums) -> bool: 
        iVal = m.inf
        jVal = m.inf
        for i in range(len(nums)):
            if nums[i] > jVal:
                return True
            if nums[i] <= iVal:
                iVal = nums[i]
            else:
                jVal = nums[i]
        return False


sol = Solution()     
print(sol.twoSum([2,7,11,15], 9))