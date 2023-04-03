### 191. Number of 1 Bits
### https://leetcode.com/problems/number-of-1-bits/

"""
Runtime | 39 ms
Beats | 17.80%
Memory | 13.8 MB
Beats | 38.30%
"""

class Solution(object):
    def hammingWeight(self, n):
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c