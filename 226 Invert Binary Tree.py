# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/
""" 
Runtime | 53 ms
Beats | 13.81%
Memory | 16.3 MB
Beats | 27.79%
"""

""" 
    The approach here is to loop through whilst the length of num isnt 1, and in each iteratiion, add the rightmost value of num
    to the current rolling total for that iteration.
    
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left,root.right = root.right,root.left
            return root

        
sol = Solution()
print(sol.invertTree([4,2,7,1,3,6,9]))