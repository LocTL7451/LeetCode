# 66. Plus One
# https://leetcode.com/problems/plus-one/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 53 ms
Beats | 41.72%
Memory | 16.3 MB
Beats | 8.52%
"""

"""
    I realised after failing to complete the problem using string and array casting upon the integer n due to TLE and out of memory for 
    string type conversions, that the easiest way is to break down the way factorial 0's are created.
    For every time n can be divided by 5, we add a 0. Simple as that.
    So I created a recursive loop for continue looping the function until it hits the base case where the current n is no longer able
    to be divided by 5
"""


import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5: return 0
        else: return (int(n/5) + self.trailingZeroes(int(n/5)))

sol = Solution()
print(sol.trailingZeroes(5))