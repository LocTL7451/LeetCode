### 1266. Minimum Time Visiting All Points
### https://leetcode.com/problems/minimum-time-visiting-all-points/

"""
Runtime | 67 ms
Beats | 39.18%
Memory | 16.4 MB
Beats | 5.31%
"""

class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        n = len(points)
        # Base case where number of point sets is one
        if n == 1:
            return 0
        retTime = 0
        # The most we can move in 1 second is 1 unit in either x and/or y direction.
        # This means the least amount of time it will take to traverse from x1,y1 to x2,y2 is max(diff(x2,x1), diff(y2,y1))
        for i in range(len(points)-1):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[i+1][0]
            y2 = points[i+1][1]
            xDiff = abs(x2 - x1)
            yDiff = abs(y2 - y1)
            retTime += max(xDiff,yDiff)    
        return retTime
    
inputVal = [[3,2],[-2,2]]
sol = Solution()
print(sol.minTimeToVisitAllPoints(inputVal))
            