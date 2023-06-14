### 19. Remove Nth Node From End of List
### https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/970750046/

"""
Runtime | 47 ms
Beats | 56.71%
Memory | 16.4 MB
Beats | 22.91%
"""

"""
    My approach for this solution was to use Floyd Warshall's tortoise and hare. 
    We first find the nth position from the start of the linked list. This is the position right before the node that we want to delete.
    We then iterate through whilst fast.next exists, and because we know that nth node will always exist in the range of the linked list, we 
    iterate through until the slow pointer reaches the position. We then set the next of the node before the node to be deleted to the 
    node after the node to be deleting, removing the reference to the node to be deleted, effectively removing it from the linked list. 
    
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

        
sol = Solution()

print(sol.removeNthFromEnd([1,2,3,4,5], 2))

        