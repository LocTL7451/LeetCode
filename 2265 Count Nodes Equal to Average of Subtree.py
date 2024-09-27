### 2265. Count Nodes Equal to Average of Subtree
### https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/?envType=daily-question&envId=2023-11-02

"""
Runtime | 50 ms
Beats | 52.82%
Memory | 17.7 MB
Beats | 23.38%
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root) -> int:
        counter = 0

        def dfs(node):
            # Used to work with variables outside of the inner scope of the function (global)
            nonlocal counter
            if not node: 
                return 0,0
            
            leftSum,leftCount = dfs(root.left) 
            rightSum,rightCount = dfs(root.right)
            
            sum = node.val + leftSum + rightSum
            count = 1 + leftCount + rightCount
            
            if(sum // count == node.val):
                counter += 1
            return sum, count

        dfs(root)
        
        return counter 
        
            
            
            