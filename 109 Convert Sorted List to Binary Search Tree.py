### 109. Convert Sorted List to Binary Search Tree
### https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

"""
Runtime | 131 ms
Beats | 75.79%
Memory | 20.1 MB
Beats | 83.67%
"""


            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        mid = self.findMid(head)
        root = TreeNode(mid.val)
        root.right = self.sortedListToBST(mid.next)
        mid.next = None
        root.left = self.sortedListToBST(head)
        return root

    def findMid(self, head):
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = None
        return slow                    
        
        
    