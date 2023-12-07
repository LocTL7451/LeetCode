### 1903. Largest Odd Number in String
### https://leetcode.com/problems/largest-odd-number-in-string/description/?envType=daily-question&envId=2023-12-07
"""
    Runtime | 23 ms
    Beats | 97.39%
    Memory | 13.9 MB
    Beats | 40.14%
"""
# Super slow and inefficient solution :( works but slow. 
# This implentation is brute forcing all substrings of nums which probably doesn't have to be done. 
import math 
class Solution:
    def largestOddNumber(self, num) -> str:
        largest = -(math.inf)
        for i in range(0, len(num)):
            for j in range(i, len(num)+1):
                currSubString = num[i:j+1]
                if int(currSubString) % 2 == 1 and int(currSubString) > largest:
                    largest = int(currSubString)
        if largest == -(math.inf):
            return ""
        else: 
            return str(largest)

sol = Solution()
print(sol.largestOddNumber("52"))