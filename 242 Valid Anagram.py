### 242. Valid Anagram
### https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 80 ms
Beats | 8.42%
Memory | 16.8 MB
Beats | 20.99%
"""

"""
    The approach to solve this problem is to store all the characters in s into a dictionary
    We then loop through t and remove an instance of the s characters from the dictionary if they
    match the current indexed character of t.
    If the resultant dictionary isn't empty, then the strings are not valid anagrams.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dupeDict = {}
        if len(s) != len(t): 
            return False
        for i in range(len(s)):
            if s[i] in dupeDict:
                dupeDict[s[i]]+=1
            else:
                dupeDict[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in dupeDict:
                if dupeDict[t[i]] == 1:
                    dupeDict.pop(t[i])
                else:
                    dupeDict[t[i]] -= 1
            else: break

        if len(dupeDict) != 0:
            return False
        else: 
            return True
sol = Solution()

print(sol.isAnagram("anagram","nagaram"))

        