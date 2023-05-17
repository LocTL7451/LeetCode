# 66. Plus One
# https://leetcode.com/problems/plus-one/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 50 ms
Beats |14.87%
Memory | 16.3 MB
Beats | 18.82%
"""

"""
    I attempted a stupid approach using stacks and popping based on whether the index was in the first or second half
    but realised the problem is so stupidly easy and achievable using a reversed version of the string of the number
    to check if the number string is a palindrome.
"""



class Solution:
    def plusOne(self, digits):
        strDigits = ""
        retArr = []
        for i in digits:
            strDigits += str(i)
        intDigits = int(strDigits)+1
        for i in str(intDigits):
            retArr.append(int(i))
        return retArr


sol = Solution()
print(sol.plusOne([4,3,2,1]))