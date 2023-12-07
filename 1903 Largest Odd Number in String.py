### 1903. Largest Odd Number in String
### https://leetcode.com/problems/largest-odd-number-in-string/description/?envType=daily-question&envId=2023-12-07
"""
Runtime | 59 ms
Beats | 35.70%
Memory | 17.9 MB
Beats | 19.52%
"""
# Super slow and inefficient solution :( works but slow. 
# This implentation is brute forcing all substrings of nums which probably doesn't have to be done. 
# import math 
# class Solution:
#     def largestOddNumber(self, num) -> str:
#         largest = -(math.inf)
#         for i in range(0, len(num)):
#             for j in range(i, len(num)+1):
#                 currSubString = num[i:j+1]
#                 if int(currSubString) % 2 == 1 and int(currSubString) > largest:
#                     largest = int(currSubString)
#         if largest == -(math.inf):
#             return ""
#         else: 
#             return str(largest)

"""
    This implementation is significantly faster using some cheeky logic that checks the string from right to left.
    A number is odd if it's last digit is an odd number, therefore we can just loop from right to left and check position by position the first instance
    of an odd number. If we find an odd number, we return the substring from position 0 all the way to the odd number positionm, which will naturally be the largest number
"""
class Solution: 
    def largestOddNumber(self, num ):
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""


sol = Solution()
print(sol.largestOddNumber("52"))