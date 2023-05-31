# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/
""" 
Runtime | 49 ms
Beats | 44.10%
Memory | 16.4 MB
Beats | 25.46%
"""

""" 
    The approach here is to count the number of instances of each character in t in s and check if they're the same. If the number of instances is
    different, then we know that the current i value is the added character.
    
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i) == t.count(i):
                pass
            else:
                return i 
        
sol = Solution()
print(sol.findTheDifference("a","aa"))