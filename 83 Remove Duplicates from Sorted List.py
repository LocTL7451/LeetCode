# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

""" 
Runtime | 280 ms
Beats | 47.53%
Memory | 21.5 MB
Beats | 57.82%
"""

""" 
    The approach here is to just loop through all the nodes in the linked list while the current node's next node exists and check if the values 
    are the same, as the caveat is that the linked list elements are sorted. We then just assign the current node's next position to the one after the 
    current next, effectively removing the middle node from the linked  list as it is no longer referenced. 
"""
class Solution:
    def deleteDuplicates(self, head):
        currNode = head
        while currNode:
            while currNode.next and currNode.val == currNode.next.val:
                    currNode.next = currNode.next.next
            currNode = currNode.next 
        return head

sol = Solution()     
print(sol.deleteDuplicates([1,1,2]))


