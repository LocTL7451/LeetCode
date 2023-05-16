# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 45 ms
Beats | 19.46%
Memory | 16.3 MB
Beats | 18.17%
"""

"""
    Super simple and primitive approach using brute force string checking.
    For string comparisons, the supposed time complexity is O(N) in best case where N is len(haystack) assuming len(needle) = 1.
    Worst case is a full comparison where N is len(haystack), M is len(needle), and worst cast brute force 
    time complexity is O(NM)
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1             
sol = Solution()
print(sol.strStr("sadcosimbad", "imb"))
                
            
        
    
