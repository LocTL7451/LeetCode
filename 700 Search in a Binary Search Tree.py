# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

"""
Runtime | 76 ms
Beats | 30.54%
Memory | 16.4 MB
Beats | 18.68%
"""

"""
    The approach to this problem is to just use base cases for each iteration. 
    Our first case is where val equals to the value of the current node, in which we return currNode which contains the subtree
    Our other two cases are where val is less than or greater than the current node, setting the new current node to left or right repsectively
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val: int):
        currNode = root
        retArr = []
        while currNode:
            if val < currNode.val:
                currNode = currNode.left
            elif currNode.val < val:
                currNode = currNode.right
            elif currNode.val == val:
                return currNode
        return

        
        
sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c","c"]))