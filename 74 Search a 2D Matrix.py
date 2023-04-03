### 74. Search a 2D Matrix
### https://leetcode.com/problems/search-a-2d-matrix/

"""
    Runtime | 29 ms
    Beats | 58.39%
    Memory | 14 MB
    Beats | 7.65%
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        #Binary Search
        row, col = len(matrix), len(matrix[0])
        i, j = 0, (row * col) - 1

        while i <= j:
            mid = (i + j) >> 1
            mid_element = matrix[mid // col][mid % col] 
            if mid_element == target:
                return True
            elif mid_element < target:
                i = mid + 1
            else:
                j = mid - 1
        return False