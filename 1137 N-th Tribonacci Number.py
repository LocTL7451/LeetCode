# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/?envType=study-plan-v2&envId=leetcode-75
""" 
Runtime | 51 ms
Beats | 17.92%
Memory | 16.3 MB
Beats | 15.32%
"""

""" 
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        d = {}
        d[0], d[1], d[2] = 0, 1, 1
        def rec(n):
            if n in d:
                return d[n]
            d[n] = rec(n-1) + rec(n-2) + rec(n-3)
            return d[n]
        return rec(n)
        
    
sol = Solution()
print(sol.tribonacci(6))