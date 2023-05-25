# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 94 ms
Beats | 59.26%
Memory | 23.1 MB
Beats | 13.27%
"""

""" 
    The approach here is to make use of python's count, which counts the number of occurances of a given parameter in a string or array. 
    This allows us to loop through all the numbers from 0 to n, in which we count the number of '1's in the binary form of each integer.
    Normally, count is an O(N) operation, but as the length of the binary string increases in proportion with the current value
    in range 0 to N, it's more of an O(log(N)) operation. This gives us an overall time complexity of O(N(log(N)))
"""
#O(NLog(N)) Solution
class Solution:
    def countBits(self, n: int):
        retArr = []
        for i in range(n+1):
            retArr.append(bin(i).count('1'))
        return retArr        
#O(N) Solution
class ONSolution:
    def countBits(self, n: int):
        retArr = []
        powerTwoCounter = 1
        for i in range(n+1):
            
            currTwoPower = 2**powerTwoCounter
            if i == 0:
                retArr.append(0)
            elif i == currTwoPower:
                retArr.append(1)
                powerTwoCounter += 1
            elif i % 2 == 0 and i != 2:
                retArr.append(retArr[-1])
            elif i % 2 == 1:
                retArr.append(retArr[-1]+1)

 
        

sol = ONSolution()     
print(sol.countBits(2))