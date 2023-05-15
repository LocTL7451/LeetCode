# 59. Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/description/
"""
    Runtime | 50 ms
    Beats | 37.67%
    Memory | 16.4 MB
    Beats | 29.40%

"""

"""
    The approach we take here is quite simple.
    We define the rules for traversing the matrix in all 4 cardinal directions, U D L R. 
    For each direction, we set a bounding variable to constrain the traversal within the unexplored region of the matrix
    We then loop over the 4 directions, closing in the bounding constraints each time a row or col has been traversed, slowly moving toward the centre of the matrix
    To handle which value is present at each index position, we use a counter variable, as each position we visit is in order spirally
"""
class Solution:
    def spiralOrder(self, n):
        
        leftBound, rightBound = 0, n-1
        upperBound, lowerBound = 0, n-1
        # Define an n*m return array for resultant matrix to be printed into.
        retMat = [[0 for i in range(n)] for j in range(n)]
        # Because we are not actually explicitly given a matrix, we have to set a counter to know what value we are currently on
        indexValCounter = 1
        
        while leftBound<=rightBound and upperBound<=lowerBound:
            for col in range(leftBound, rightBound+1):
                retMat[upperBound][col] = indexValCounter
                indexValCounter += 1
            upperBound += 1
            for row in range(upperBound, lowerBound + 1):
                retMat[row][rightBound] = indexValCounter
                indexValCounter +=1
            rightBound -= 1
            # We have to set  
            for col in range(rightBound, leftBound-1, -1):
                retMat[lowerBound][col] = indexValCounter
                indexValCounter +=1
            lowerBound -= 1
            for row in range(lowerBound, upperBound-1, -1):
                retMat[row][leftBound] = indexValCounter
                indexValCounter +=1
            leftBound += 1
        return retMat
            
sol = Solution()
print(sol.spiralOrder(3))
                
            
        
    
