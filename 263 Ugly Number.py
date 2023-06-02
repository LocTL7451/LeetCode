# 263. Ugly Number
# https://leetcode.com/problems/ugly-number/

""" 
Runtime | 45 ms
Beats | 43.4%
Memory | 16.3 MB
Beats | 38.69%
"""

""" 
    The approach here is divide n by 5 until you can't, then by 3 then by 2, resulting in 1 or not 1 if n has another prime factor. 
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 5 == 0:
            n /= 5
        while n % 3 == 0:
            n /= 3
        while n % 2 == 0:
            n /= 2
        return n == 1
sol = Solution()
print(sol.isUgly(14))