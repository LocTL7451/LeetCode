# 120. Triangle
# https://leetcode.com/problems/triangle/

""" 
Runtime | 74 ms
Beats | 53.60%
Memory | 17.4 MB
Beats | 24.31%
"""

""" 
    I'd assume the most common approach is to utilize memoization or tabulation in a DP solution.
    This however has an average time complexity of O(N)^2.
    We can approach this question by using cumulative sumation, and thinking of the triangle as a right angle triangle.
    At any given position in the triangle, we replace the element with a sum of the minimum value of access nodes in the 
    depth above the current, adding the current value to the min sum of previous values to create a rolling cumulative sum.
    There are however, base cases that we must consider. At either side of each depth of the triangle, 
    only the outermost position from the previous depth can act as an access point to the current node.
    Because of this, we write logic to handle 3 cases, front, back and middle of each level.
    The front and back only take the value from the access node, as that's the only triangle node that can get to the current node.
    For the middle nodes, we take a min check of the 2 previous layer nodes that can access the current node.
    By the end of the for loop iteration, we end up with a list of all the optimised minimum values for each path taken up until
    position i in the final depth.
    To find the overall min path cost, we just grab the min of the bottom layer of the triangle.
"""
class Solution:
    def minimumTotal(self, triangle) -> int:
        for level in range(1,len(triangle)):
            for index in range(len(triangle[level])):
                #First position in the level
                if index == 0:
                    triangle[level][index] = triangle[level][index] + triangle[level-1][index] 
                #Last position in the level                
                elif index == len(triangle[level])-1:
                    triangle[level][index] = triangle[level][index] + triangle[level-1][index-1]
                else:
                    triangle[level][index] = min(triangle[level-1][index],triangle[level-1][index-1]) + triangle[level][index]
        return min(triangle[-1])
                 

sol = Solution()     
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))