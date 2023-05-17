# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 56 ms
Beats | 12.11%
Memory | 16.4 MB
Beats | 22.65%
"""

"""
    The approach here is to turn the string into an array of strings, with each position containing 
    a word. We then simply use list splicing to reverse the string and join each position back
    together, spacing each element with a space.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        sRev = s[::-1]
        joinedS = " ".join(sRev)
        return joinedS

             

sol = Solution()

print(sol.reverseWords("  hello world  "))

        