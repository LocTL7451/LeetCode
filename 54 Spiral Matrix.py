### 54. Spiral Matrix
### https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 45 ms
Beats | 45.31%
Memory | 16.2 MB
Beats | 57.58%
"""

"""
    The approach for this question is very similar to problem #59 Spiral Matrix II
    The following is an exerpt from my comment in problem 59:
    
        The approach we take here is quite simple.
        We define the rules for traversing the matrix in all 4 cardinal directions, U D L R. 
        For each direction, we set a bounding variable to constrain the traversal within the unexplored region of the matrix
        We then loop over the 4 directions, closing in the bounding constraints each time a row or col has been traversed, slowly moving toward the centre of the matrix
        To handle which value is present at each index position, we use a counter variable, as each position we visit is in order spirally

    The difference between spiral matrix II and this problem is that instead of going in spiral ordered positions
    using an n bounding size, we instead just reference the position from the original matrix.
    We also change the code to make use of N for column size and M for row size for the matrix operations.
"""
class Solution:
    def spiralOrder(self, matrix) :
        n = len(matrix)
        m = len(matrix[0]) 
        upperBound = 0
        lowerBound = n-1 
        leftBound = 0 
        rightBound = m-1
        result = []
        
        while len(result) < n * m:
            for i in range(leftBound, rightBound+1):
                result.append(matrix[upperBound][i])
            upperBound += 1
            for i in range(upperBound, lowerBound+1):
                result.append(matrix[i][rightBound])
            rightBound -= 1
            if upperBound <= lowerBound:
                for i in range(rightBound, leftBound-1, -1):
                    result.append(matrix[lowerBound][i])
                lowerBound -= 1
            if leftBound <= rightBound:
                for i in range(lowerBound, upperBound-1, -1):
                    result.append(matrix[i][leftBound])
                leftBound += 1
        
        return result