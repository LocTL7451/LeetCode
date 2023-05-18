# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 108 ms
Beats | 59.35%
Memory | 20.4 MB
Beats | 20.31%
"""

"""
    The approach here is to apply the tortoise and hare algorithm, where
    we make use of two pointers, one being slower than the other. 
    The fast pointer will always reach the end of the linked list before
    the slow one will, which means that if the pointers ever meet (due to fast
    reaching the cycle node pointer back through the linked list), then we 
    know that there is a cycle in the linked list.  
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slowPointer = head
        fastPointer = head
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if fastPointer == slowPointer:
                return True
        return False
                