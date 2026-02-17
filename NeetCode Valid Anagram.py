""" 
    Runtime
    31ms
    |
    Beats 100.00%
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set = {}
        for i in s: 
            if i in set:
                set[i] += 1
            else:
                set[i] = 1
        for j in t:
            if j in set:
                if set[j] == 1:
                    del set[j]
                else: 
                    set[j] -= 1
            else: return False
        return len(set) == 0
s = "racecar"
t= "carrace"    
sol = Solution()     
print(sol.isAnagram(s,t))