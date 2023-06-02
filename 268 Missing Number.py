# 268. Missing Number
# https://leetcode.com/problems/missing-number/

""" 
Runtime | 144 ms
Beats | 52.54%
Memory | 17.8 MB
Beats | 10.86%
"""

""" 
    The approach here is realise that to find the missing number in a number set of n in order numbers, we just have to sum all numbers 
    up until N, and then minus all the numbers in the array from that sum. This results in the number that is missing from the array. 
"""

class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        cumulSum = 0
        for i in range(n):
            cumulSum += (i+1)
            cumulSum -= nums[i]
        return cumulSum
        
sol = Solution()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))