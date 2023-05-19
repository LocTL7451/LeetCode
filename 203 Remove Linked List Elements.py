# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/

"""
Runtime | 102 ms
Beats | 11.4%
Memory | 18 MB
Beats | 10.73%
"""

"""
    The approach here is to make use of two pointers, one starting at the front of the string and one starting at the back
    Due to python strings being immutable objects, we turn the input string into an array which is a mutable object.
    We then iterate through the list moving the pointer towards each other, and check if either pointer is on a vowel
    If both pointers are on vowels, we swap the index position of both of the elements.
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):
        prevNode = None
        currNode = head 
        while currNode != None:
            if currNode.val == val:

                if prevNode != None:
                    prevNode.next = currNode.next

                else: 
                    head = currNode.next
                    print(head)

                currNode = currNode.next
            else:
                currNode,prevNode = currNode.next,currNode
        return head

sol = Solution()
print(sol.removeElements([1,2,6,3,4,5,6],6))