# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&id=leetcode-75
""" 
Runtime | 55 ms
Beats | 16.19%
Memory | 16.3 MB
Beats | 32.9%
"""

""" 
    The approach for this problem is super simple. 
    The main logic involves looping through the gain array and adding the value at the index to 
    overallAlt. For each time overallAlt is altered, we check it against the current max value.
"""

class Solution:
    def largestAltitude(self, gain) -> int:
        retArr = []
        currMax = 0
        overallAlt = 0
        for i in gain:
            overallAlt += (i)

            if currMax < overallAlt:
                currMax = overallAlt
            retArr.append(overallAlt)
        return currMax
    
    
sol = Solution()     
print(sol.largestAltitude([-5,1,5,0,-7]))