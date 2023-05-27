# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/submissions/958163211/?envType=study-plan-v2&id=leetcode-75
""" 
Runtime | 56 ms
Beats | 18.1%
Memory | 17.9 MB
Beats | 45.41%
"""

""" 
    The approach here is to loop through all the positions in the linked list, and for each position,
    the goal is essentially to remove the forward reference from the current node currNode to 
    the next node, temp. By doing this, we can set the next node as the previous node,
    essentially reversing the order of the list. 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if not head:
            return head
        else:
            prevNode = None
            while head:
                temp = head.next
                head.next = prevNode
                prevNode = head
                head = temp
        return prevNode


sol = Solution()     
print(sol.twoSum([2,7,11,15], 9))