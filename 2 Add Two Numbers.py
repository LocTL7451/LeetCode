# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

""" 
Runtime | 86 ms
Beats | 19.76%
Memory | 16.5 MB
Beats | 13.58%
"""

""" 
We loop through both linked lists and append each value to a rolling total, which we then reconstruct a new linked list for and
find correct positions by integer dividing the carry value by 10
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = currNode = ListNode(0)
        carryVal = 0
        while l1 or l2 or carryVal:
            if l1:
                carryVal += l1.val
                l1 = l1.next
            if l2:
                carryVal += l2.val
                l2 = l2.next
            currNode.next = ListNode(carryVal % 10)
            currNode = currNode.next
            carryVal //= 10
        return head.next

    
sol = Solution()
print(sol.getConcatenation("capiTalIze tHe titLe"))