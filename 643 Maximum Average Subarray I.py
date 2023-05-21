# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 1196 ms
Beats | 73.37%
Memory | 28.3 MB
Beats | 27.24%
"""

""" 
    The approach for this problem is to use an initial summation to save computational power for large number sets.
    We start by finding the summation of elements positioned 0 through to k. This gives us the sum value for the first sliding window.
    To slide the window across by 1 position without having to recalculate the sum, we minus the ith value (front of the previous window)
    and add the i+kth value (back of the new window).
    If this value is greater than the previous window's summation, we replace it and return the max value over k for the final result.
"""

class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        n = len(nums)
        if n == 1:
            return float(nums[0])
        currMax = currSum = sum(nums[:k])
        for i in range(n-k):
            currSum += nums[i+k]
            currSum -= nums[i]
            currMax = max(currMax,currSum)
        return currMax/k
            
            

    
sol = Solution()     
print(sol.findMaxAverage([1,12,-5,-6,50,3],4))