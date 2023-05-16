# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 75 ms
Beats | 34.80%
Memory | 16.3 MB
Beats | 30.32%
"""

"""
    Super simple and primitive approach using brute force string checking.
    For string comparisons, the supposed time complexity is O(N) in best case where N is len(haystack) assuming len(needle) = 1.
    Worst case is a full comparison where N is len(haystack), M is len(needle), and worst cast brute force 
    time complexity is O(NM)
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:    
        ransomDict = {}
        
        # Seeding the dictionary with all the letters in ransomnote
        for i in ransomNote:
            if i not in ransomDict:
                ransomDict[i] = 1
            else:
                ransomDict[i] += 1
        
        for i in magazine:
            if i in ransomDict:
                if ransomDict[i] > 1:
                    ransomDict[i] -= 1
                else: 
                    ransomDict.pop(i)
        if len(ransomDict) != 0:
            return False
        else:
            return True
                
                
                       
sol = Solution()
print(sol.canConstruct("a", "b"))
                
 
        
    
