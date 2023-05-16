# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 291 ms
Beats | 5.24%
Memory | 26.6 MB
Beats | 5.21%
"""

"""
    My approach for this solution was to split up the nums array into two corresponding arrays, one for prefixes and one for suffixes.
    For every index "i" in nums, we find the cumulative product for all positions up until i on the left side (prefix product sum) 
    and the right side (suffix product sum). 
    By multiplying the two prefix/suffix values at any given position, we are given a resulting number that represents the product of the array 
    without the current index value of num.
"""

import itertools
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefixProd = [0 for _ in range(n)]
        suffixProd = [0 for _ in range(n)]
        retArr = [0 for _ in range(n)]
        print("{}\n{}\n{}\n".format(prefixProd,suffixProd,retArr))
        # Setting up the initial value for both arrays
        prefixProd[0] = 1
        suffixProd[n-1] = 1 
        
        for i in range(1,n):
            prefixProd[i] = prefixProd[i-1] * nums[i-1]
        print("Prefix array: {}".format(prefixProd))
        for i in range(n-2, -1, -1):
            suffixProd[i] = suffixProd[i+1] * nums[i+1]
        print("Suffix array: {}".format(suffixProd))
        for i in range(n):
            retArr[i] = prefixProd[i] * suffixProd[i]
        return retArr
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
                
            
        
    
