### 2390. Removing Stars From a String
### hhttps://leetcode.com/problems/removing-stars-from-a-string/description/
"""
Runtime | 434 ms
Beats | 19.1%
Memory | 15.7 MB
Beats | 35.9%
"""

class Solution:
    """
        We approach the solution by identifying a data structure that we can use to store the most recent element in the string
        To do this, we apply the stack, pushing each element onto the string if it isnt a *
        If the element is a *, we pop the most recent element assuming that the stack isn't empty (symbolizing that the first element isn't a *)
    """
    def removeStars(self, s: str) -> str:
        stack = [] 
        for i in range(len(s)):
            if s[i] == "*" and len(stack) > 0:
                stack.pop()
            else:
                stack.append(s[i])
    
        return ("".join(stack))