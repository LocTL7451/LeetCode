# 2027. Minimum Moves to Convert String
# https://leetcode.com/problems/minimum-moves-to-convert-string/submissions/957734171/

""" 
Runtime | 280 ms
Beats | 47.53%
Memory | 21.5 MB
Beats | 57.82%
"""

""" 
    The approach here is to loop through all positions of s, and check for any instance of X in the list. If we find an instance of X, we skip the 
    next 3 positions as it doesn't matter if they're O or X, we will just add 1 to the return array and move on. 
"""
class Solution:
    def minimumMoves(self, s: str) -> int:
        ret = 0
        i= 0
        while i in range(len(s)):
            if s[i] == "X":
                ret+=1
                i+=3
            else:
                i+=1
        return ret
                
           
                
            
            
            

sol = Solution()     
print(sol.minimumMoves("XXOX"))


