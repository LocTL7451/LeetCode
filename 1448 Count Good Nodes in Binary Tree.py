# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75

""" 
Runtime | 309 ms
Beats | 5.30%
Memory | 35.4 MB
Beats | 18.6%
"""

""" 
    The approach to solve this solution is to utilise a common DFS pattern in coding questions. These questions usually entail 
    traversing through the tree and keeping track of some arbitrary value, in this case being the current max val of the traversed nodes
    so far leading up to the current node. The way we do this is through using DFS, as DFS allows us to traverse to from the root
    to all leaf nodes. This is facilitated through the usage of the Queue data structure, allowing us to walk down each path node by node 
    by appending to the end of the queue and popping from the front (position 0) of the queue. 
    For each node, we check if the node's value is greater than the max val of the current traversed path, incrementing the return 
    value if it is. We then continue traversing the tree by adding the left and right nodes of the current node if they exist, adding
    the extra parameter of the max val which will only change if the current node's value is greater than the current cumulative max.
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
        
        while dfsQueue:
            currNode = dfsQueue.pop(0)
            if currNode[0].val > currNode[1]:
                ret+=1
            if currNode[0].left:
                dfsQueue.append((currNode[0].left, max(currNode[0].val, currNode[1])))
            if currNode[0].right:
                dfsQueue.append((currNode[0].right, max(currNode[0].val, currNode[1])))
        return ret
        
sol = Solution()
print(sol.isUgly(14))