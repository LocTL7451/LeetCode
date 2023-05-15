# 1721. Swapping Nodes in a Linked List
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""
    Runtime | 917 ms
    Beats | 98.99%
    Memory | 50.9 MB
    Beats | 18.73%

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
    The approach we take here is to search for the nodes that contain the kth position
    in the linked list and the n-kth position in the linked list
    
    Once we find these two nodes, we just have to swap the values of the nodes with each other. 
"""
class Solution:
    def swapNodes(self, head, k):
        
        firstkNode = head
        lastkNode = head
        for i in range(1, k):
            firstkNode = firstkNode.next
        # At this point, firstkNode contains a reference to the kth node from the left of the linked list
        """
            Here, we apply the two pointer method, as the difference from 0th position to kth position on the left side
            will also be the difference between the nth position and the n-kth position
            Hence, we will keep iterating from position firstkNode until we cannot iterate further, indicating we have reached the end of the linked list
            where the left side of the sliding window two pointer will be the n-kth position.
            
            Another approach would be to calculate the number of positions we need to iterate over and simply for loop it. 
        """
        endReferencePointer = firstkNode
        while endReferencePointer.next:
            lastkNode = lastkNode.next
            endReferencePointer = endReferencePointer.next
        # Here we simply swap the value of the two nodes with each otehr 
        
        lastkNode.val,firstkNode.val = firstkNode.val,lastkNode.val
        return head 
    
    
