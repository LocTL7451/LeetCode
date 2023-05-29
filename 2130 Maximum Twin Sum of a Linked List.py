# 2130. Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 919 ms
Beats | 53%
Memory | 58.3 MB
Beats | 8.65%
"""

""" 
The approach for this question is to make use of a variation on Floyd's tortoise and hare algorithm along with the stack data structure.
We start by iterating through the first n/2 positions in the linked list, adding each value of the node to the stack.
Once we reach the end of the first while loop, we then loop through the last n/2 nodes in the linked list and check if the current max value
is greater than the current indexed list node value plus the value popped from the top of the stack.  
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head) -> int:
        if head.next.next == None:
            return head.val + head.next.val
        stack = [] 
        maxVal = 0 
        fastPointer = head
        slowPointer = head
        prevPointer = head
        while fastPointer:

            fastPointer = fastPointer.next.next
            prevPointer = slowPointer
            slowPointer = slowPointer.next
            stack.append(prevPointer.val)
        while slowPointer:
            maxVal = max(maxVal,stack.pop(-1)+slowPointer.val)
            slowPointer = slowPointer.next
        return slowPointer
                
            
            
            

sol = Solution()     
print(sol.minimumMoves("XXOX"))


