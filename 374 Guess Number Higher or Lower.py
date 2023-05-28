# 374. Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
""" 
Runtime | 56 ms
Beats | 18.1%
Memory | 17.9 MB
Beats | 45.41%
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        midNum = n//2
        left = 0
        right = n
        guessNum = guess(midNum)
        while(guessNum) != 0 and right > left:
            if guessNum == 1:
                left = midNum +1
                midNum = (left+right) // 2
                guessNum = guess(midNum)
            else:
                right = midNum - 1
                midNum = (left+right)//2
                guessNum = guess(midNum)
        return midNum


sol = Solution()
print(sol)