# 872. Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75
""" 
Runtime | 42 ms
Beats | 65.72%
Memory | 16.6 MB
Beats | 11.55%
"""

""" 
    The approach here is to make use of the DFS algorithm, in which we use a stack to traverse as far down vertically as possible until running into
    leaf nodes. We do a left to right DFS traversal to ensure that the leaf elements are checked in relative order. We use DFS to create a list of 
    leaf node values for both tree roots, then we check to see if the arrays are the same. 
    
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        nodeQueue = []
        root1Arr = []
        root2Arr = []
        
        if not root1:
            return False
        elif not root1.left and not root1.right and not root2.left and not root2.right:
            return (root1.val == root2.val)
        else:
            currNode = root1
            while True:
                if len(nodeQueue) == 0 and currNode == root1:
                    if currNode.right:
                        nodeQueue.append(currNode.right)
                    if currNode.left:
                        nodeQueue.append(currNode.left)
                    if not currNode.left and not currNode.right:
                        root1Arr.append(currNode.val)
                elif len(nodeQueue) == 0 and currNode != root1:
                    break
                else:
                    currNode = nodeQueue.pop(-1)
                    if currNode.right: 
                        nodeQueue.append(currNode.right)     
                    if currNode.left:
                        nodeQueue.append(currNode.left)           
                    if not currNode.left and not currNode.right:
                        root1Arr.append(currNode.val)
        print(root1Arr)
        nodeQueue = []
        if not root2:
            return False
        else:
            currNode = root2
            while True:
                if len(nodeQueue) == 0 and currNode == root2:
                    if currNode.right:
                        nodeQueue.append(currNode.right)
                    if currNode.left:
                        nodeQueue.append(currNode.left)
                    if not currNode.left and not currNode.right:
                        root2Arr.append(currNode.val)
                elif len(nodeQueue) == 0 and currNode != root2:
                    break
                else:
                    currNode = nodeQueue.pop(-1)
                    if currNode.right: 
                        nodeQueue.append(currNode.right)     
                    if currNode.left:
                        nodeQueue.append(currNode.left)           
                    if not currNode.left and not currNode.right:
                        root2Arr.append(currNode.val)
        print(root2Arr)
        if root1Arr == root2Arr:
            return True
        else:
            return False
        
sol = Solution()
print(sol.invertTree([4,2,7,1,3,6,9]))