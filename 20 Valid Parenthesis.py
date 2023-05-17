# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 52 ms
Beats | 9.68%
Memory | 16.3 MB
Beats | 23.42%
"""

"""
    My approach here is to map each closing bracket to an opening bracket using a dictionary.
    If the current checked character is an opening bracket, it is pushed onto the stack.
    If the current checked character is a closing bracket, the popped(top most) value of the stack is checked to see 
    if the bracket types match, and rejected if they are not. 
"""


class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"]":"[", "}":"{", ")":"("}
        stack = []
        for i in range(len(s)):
            if s[i] in dict.values():
                stack.append(s[i])
            elif s[i] in dict.keys():
                if len(stack) == 0 or dict[s[i]] != stack.pop():
                    return False
            else:
                return False
        return stack == []