### 1342. Number of Steps to Reduce a Number to Zero 
### https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

"""
    Runtime | 23 ms
    Beats | 97.39%
    Memory | 13.9 MB
    Beats | 40.14%
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num > 0:
            if num%2 == 1:
                num = num - 1
                counter+=1
            else: 
                num = num/2
                counter+=1
            
        return counter