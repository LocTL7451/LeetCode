# 709. To Lower Case
# https://leetcode.com/problems/to-lower-case/description/

""" 
Runtime | 45 ms
Beats | 43.4%
Memory | 16.3 MB
Beats | 38.69%
"""

""" 
    The approach here is to make use of python's lower() function, which iterates through the string and turns every char into lower case. 
"""

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
sol = Solution()
print(sol.toLowerCase("tEsT"))