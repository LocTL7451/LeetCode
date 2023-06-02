# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75

""" 
Runtime | 45 ms
Beats | 43.4%
Memory | 16.3 MB
Beats | 38.69%
"""

""" 
    The approach here is divide n by 5 until you can't, then by 3 then by 2, resulting in 1 or not 1 if n has another prime factor. 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math as m 
class Solution:
    def goodNodes(self, root) -> int:
        dfsQueue = []
        ret = 0
        dfsQueue.append((root,-m.inf))
        
        
        
        
sol = Solution()
print(sol.isUgly(14))