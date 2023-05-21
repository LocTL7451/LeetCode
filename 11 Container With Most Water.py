# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&id=leetcode-75

"""
Runtime | 694 ms
Beats | 87.91%
Memory | 29.5 MB
Beats | 14.46%
"""

"""
    The approach here is to keep 2 pointers, one at the front and one at the back of height. We then loop whilst the pointers don't overlap
    or pass over each other, with each iteration calculating the area of the current rectangle formed by the two pointers. As we only need to store the max 
    area at any given time, we simply check if the current area is greater or less than the current maximum area. 
    As this is a greedy approach, our goal here is to find the bar with the largest height, hence we iterate forward the pointer
    that contains a smaller value in hopes of finding a position with a higher value.
"""

class Solution:
    def maxArea(self, height) -> int:
        n = len(height)
        frontPointer = 0
        endPointer = n-1
        maxArea = 0
        if n == 0:
            return maxArea
        
        while endPointer > frontPointer:
            currHeight = min(height[endPointer],height[frontPointer]) 
            currWidth = endPointer - frontPointer
            currArea = currHeight * currWidth
            
            if currArea > maxArea:
                maxArea = currArea
            else:
                if height[endPointer] > height[frontPointer]:
                    frontPointer += 1
                else:
                    endPointer -= 1
                    
        return maxArea
sol = Solution()
print(sol.maxArea([1]))