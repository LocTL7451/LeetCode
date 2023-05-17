### 20. Valid Parentheses
### https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 45 ms
Beats | 45.31%
Memory | 16.2 MB
Beats | 57.58%
"""

"""
"""
class Solution:
    def isValid(self, s: str) -> bool:
        checkStack = []
        for i in range(len(s)):
            if s[i] in ["{","(","["]:

                checkStack.append(s[i])
                print("push {}".format(checkStack))
            elif s[i] in ["}",")","]"]:
                print(checkStack[-1])
                
                if s[i] == ")" and checkStack[-1] == "(":
                    checkStack.pop(-1)
                    print("pop {}".format(checkStack))
                elif s[i] == "}" and checkStack[-1] == "{":
                    checkStack.pop(-1)
                    print("pop {}".format(checkStack))
                elif s[i] == "]" and checkStack[-1] == "[":
                    checkStack.pop(-1)
                    print("pop {}".format(checkStack))
        if len(checkStack) != 0:
            return False
        else: 
            return True
sol = Solution()
print(sol.isValid("()"))