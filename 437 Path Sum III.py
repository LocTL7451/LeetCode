# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/?envType=study-plan-v2&envId=leetcode-75
""" 
Runtime | 51 ms
Beats | 17.92%
Memory | 16.3 MB
Beats | 15.32%
"""

""" 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = {}
        d[0] = 1
        def dfsTraversal(root, val):
            counter = 0
            if root:
                val += root.val
                counter = d[val-targetSum]
                d[val] += 1
                counter += dfsTraversal(root.left,val) + dfsTraversal(root.right,val)
                d[val] -= 1
            return val
        return dfsTraversal(root,0)
sol = Solution()
print(sol.tribonacci(6))