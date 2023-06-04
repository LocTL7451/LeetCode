# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

""" 
Runtime | 50 ms
Beats | 47.84%
Memory | 16.4 MB
Beats | 26.36%
"""

""" 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val <= list2.val: #1
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else: #2
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    
sol = Solution()
print(sol.getConcatenation("capiTalIze tHe titLe"))