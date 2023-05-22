# 2352. Equal Row and Column Pairs
# https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 1747 ms
Beats | 10.75%
Memory | 38.5 MB
Beats | 5.2%
"""

""" 
    The approach to solving this problem is to make use of math theory relating to identity matrices. We can transpose a matrix by 90 degrees
    if we multiply is by a particular identity matrix matching it's n*n size. Luckily for us, numpy (refered to as np here for the sake of convenience)
    provides us with the means to facilitate doing that. We make use of transpose from np to transpose the original grid. This means we can directly
    compare the rows and cols of grid, as the cols of grid become rows in the transposed matrix. 
    
    We then just keep a counter and loop through every line of the original matrix to see if it exists as a row in the transposed matrix, which represents
    the cols in the original matrix.
    
"""
import numpy as np
class Solution:
    def equalPairs(self, grid) -> int:
        grid = np.array(grid)
        counter = 0
        transposedGrid = np.transpose(grid)
        for i in range(len(grid)):
            for j in range(len(transposedGrid)):
                if np.array_equal(grid[i],transposedGrid[j]):
                    counter += 1
                    
        return counter
        
                 

sol = Solution()     
print(sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))