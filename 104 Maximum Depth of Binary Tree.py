# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 48 ms
Beats | 56.21%
Memory | 18.7 MB
Beats | 15.80%
"""

""" 
    The approach here is to use recursion to traverse down the binary tree. We could use a DFS solution, but that would be overcomplicating a very 
    easily achievable recursive solution. For each node, we return to the previous node, the max between the right and left child node's depths.
    If the referenced node doesn't exist, ie we reach the end of a branch, we return 0, as we always add 1 to whatever max value we calculate. 
"""
# Definition for the binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if root == None: 
            return 0
        else:
            return 1 + max(self.maxDepth(root.right),self.maxDepth(root.left))


            

 
        

sol = Solution()     
print(sol.maxDepth([3,9,20,null,null,15,7]))