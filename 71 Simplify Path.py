# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 48 ms
Beats | 7.75%
Memory | 16.4 MB
Beats | 6.41%
"""

"""
    The apporach here was to turn the path string into an array of strings. From this we are left with only ".", ".." and words.
    We then loop throught the array and simplify the path by checking if the current position is a word and pushing it onto the stack.
    If it is not a word and if it is a "..", we check to make sure the stack isnt empty, then we pop the most recent word off the stack, fulfilling
    the role of the "..".
    We then reconstruct the array into a string, adding "/" between each word and removing the trailing "/" at the end.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        pathArr = path.split("/")
        print(pathArr)
        stack = []
        for i in pathArr:
            if i == ".." and stack:
                stack.pop()
            elif i not in [".", "", ".."]:
                stack.append(i)
        retPath = "/"
        for i in stack:
            retPath = retPath + i + "/"
        if len(retPath) > 1:
            retPath = retPath[:len(retPath)-1]
       
        return retPath