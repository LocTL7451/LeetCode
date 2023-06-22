# 100. Same Tree
# https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150

""" 
Runtime | 42 ms
Beats | 79.18%
Memory | 16.3 MB
Beats | 87.55%
"""

""" 
    The approach for this problem was to use function recursion to recursively call isSameTree, passing through each root node's left and right nodes until the 
    function returns either a true or false. For each call of isSameTree, the function will first check if one of the nodes has reached the bottom of the branch, hence
    having the value of None, and check if just one right/left node is None or if both are None, returning True if both node ends are None or if just 1 is None.
    The function then checks to see if both the values of the current nodes are the same, returning true to the callback if they are or false if they are different. This 
    resulting binary flag will then trickle back up the callback chain, affecting the isSameTree(left,left) and isSameTree(right,right) check and either breaking it with
    a false or validating it with a true.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
sol = Solution()
print(sol.isUgly(14))