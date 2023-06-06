# 1290. Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
""" 
Runtime | 48 ms
Beats | 33.45%
Memory | 16.4 MB
Beats | 9.71%
"""

""" 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binStr = ""
        while head:
            binStr = binStr + str(head.val)
            head = head.next
        return int(binStr,2)
        
    
sol = Solution()
print(sol.getDecimalValue())