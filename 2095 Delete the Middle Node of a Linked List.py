# 2095. Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 1712 ms
Beats | 75.58%
Memory | 63 MB
Beats | 40.97%
"""

""" 
    The approach here is to make use of a variation of Floyd's tortoise and hare algorithm, where instead of using it to find a cycle in the 
    linked list, we instead use it to traverse through and search for the end of the linked list. 
    We do this by setting 3 pointers in the linked list, "fast" which travels 2 nodes, "slow" which travels 1 node, and "prevSlow" which travels
    to the position of "slow" - 1 node each time. In doing so, fast will reach the end of the linked list twice as fast as slow will, hence 
    slow will contain the position of the middle element of the linked list. Keep in mind we have to handle 3 base cases, one for odd linked list
    length, one for even and one for where the length of the linked list is 1.
    To solve the 1 length base case, we simply return head.next, returning an empty node. 
    To solve the even length base case, the fast pointer will reach n-1 position, where n is the length of the linked list, denoting the last 
    position in the linked list. Due to the nature of skipping 2 nodes each time and None type not having a .next, we instead check if .next exists, 
    which suggests that .next.next is None and therefore traversable. 
    To solve the odd length base case, the fast pointer will stop at n-2 position, meaning that we know .next exists as n-1's node, therefore stepping
    over it into n will result in None, causing the while loop to stop. 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head.next
        prevSlowPointer = head
        fastPointer = head
        slowPointer = head
        while fastPointer:
            if fastPointer.next:
                fastPointer = fastPointer.next.next
            else:
                fastPointer = fastPointer.next
                break

            prevSlowPointer = slowPointer
            slowPointer = slowPointer.next
        prevSlowPointer.next = slowPointer.next
        return head

           
                
            
            
            

sol = Solution()     
print(sol.minimumMoves("XXOX"))


