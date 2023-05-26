# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 1365 ms
Beats | 49.85%
Memory | 30.7 MB
Beats | 37.65%
"""

""" 
    The approach here is to use a traversing monotonic stack, in which we iterate through the array of temperatures and keep two vars for
    the enumerated array, index and temp. We then make use of the mono stack and backwards resolve the stack, in which if the currently checked
    temperature is greater than the temperature of the top of the stack, we set the return arrays value at the top of the stacks position
    to the difference in indices from the current temp and the top of the stack. 
    We while loop through this, effectively resolving the entire stack backwards until all the positions in the return array are filled in.
"""
class Solution:     
        def dailyTemperatures(self, temperatures):
            n = len(temperatures)
            retArr = [0] * n
            monoStack = []
            if n == 1:
                return 0 
            for index,temp in enumerate(temperatures):
                while len(monoStack) > 0 and temp > temperatures[monoStack[-1]]:
                    prev = monoStack.pop(-1)
                    retArr[prev] = index - prev
                monoStack.append(index)
            return retArr
                
                
           
                
            
            
            

sol = Solution()     
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))

