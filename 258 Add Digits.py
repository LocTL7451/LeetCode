# 258. Add Digits
# https://leetcode.com/problems/add-digits/
""" 
Runtime | 53 ms
Beats | 13.81%
Memory | 16.3 MB
Beats | 27.79%
"""

""" 
    The approach here is to loop through whilst the length of num isnt 1, and in each iteratiion, add the rightmost value of num
    to the current rolling total for that iteration.
    
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            strNum = str(num)
            num = 0
            for i in range(len(strNum)):
                num += int(strNum[i])
        return num
        
sol = Solution()
print(sol.addDigits(38))