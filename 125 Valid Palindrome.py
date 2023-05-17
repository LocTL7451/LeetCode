### 125. Valid Palindrome
### https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 59 ms
Beats | 40.54%
Memory | 17.9 MB
Beats | 13.52%

"""

"""
    My approach here is to preprocess the s string into a form that is easily checkable.
    To do this, we first send all characters in the string to lower case. 
    We then use an one line for loop to add all indices in the string that are of alphanumeric value
    into a new string.
    We then do the classic palindrome check of reversing the string and checking if it matches the 
    same string back to forth.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = ''.join(c for c in s if c.isalnum())
        sRev = s[::-1]
        if s == sRev:
            return True
        else:
            return False
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))

        