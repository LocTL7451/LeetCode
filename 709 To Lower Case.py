# 709. To Lower Case
# https://leetcode.com/problems/to-lower-case/description/

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
    def toLowerCase(self, s: str) -> str:
        return s.lower()
sol = Solution()
print(sol.toLowerCase("tEsT"))