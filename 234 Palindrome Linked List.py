# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/
""" 
Runtime | 788 ms
Beats | 56.52%
Memory | 49.3 MB
Beats | 18.45%
"""

""" 
    Whilst there are more efficient ways of approaching the problem, we make use of the traditional way of finding out if a string is a palindrome - by
    flipping it backwards and checking if it reads the same. 
    We first loop through the linked list, adding each node's value to an array, then flipping the array and checking if the arrays are
    equal.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        currNode = head
        arr = []
        while currNode:
            arr.append(currNode.val)
            currNode = currNode.next
        if arr == arr[::-1]:
            return True
        else:
            return False 
        
sol = Solution()
print(sol.isPalindrome([1,2,2,1]))