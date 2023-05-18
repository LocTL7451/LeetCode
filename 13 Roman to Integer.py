# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 80 ms
Beats | 5.49%
Memory | 16.3 MB
Beats | 13.71%
"""

"""
    The approach here is to replace all instances of strange roman numeral rules with the actual value they represent.
    An example of this is IV, which is 5-1 = 4.
    We then check the hash map of roman numeral to integer and find the sum of all the positions
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        stack = []
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")
        refDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            stack.append(s[i])
        counter = 0
        for i in stack:
            counter += refDict[i]
        return counter
    
sol = Solution()
print(sol.romanToInt("MCMXCIV"))
        