# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/?envType=study-plan-v2&id=leetcode-75
""" 
Runtime | 56 ms
Beats | 18.1%
Memory | 17.9 MB
Beats | 45.41%
"""

""" 

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printLinkedList(self,head):
        #print("DEBUG ENTERED PRINTLINKEDLIST")
        currNode = head
        retArr = []
        while currNode:
            #print("Current Node's Value: {}".format(currNode.val))
            retArr.append(currNode.val)
            currNode = currNode.next
        print(retArr)

    def oddEvenList(self, head):
        if not head: 
            return head

        evenStart = head 
        oddStart = head
        evenEnd = head
        oddEnd = head
        if head.val % 2 == 0:
            while evenEnd and evenEnd.val % 2 == 0:
                evenEnd = evenEnd.next
                
            if evenEnd:
                
            else:
                return head
        

class LinkedListNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.end = None
    def insert(self,val) -> None:
        # Checking to see if our linked list already has values within the reference list
        if self.head and self.end:
            #print("Inserted value {} into the linked list".format(val))
            self.end.next = LinkedListNode(val)
            self.end = self.end.next
        # If the list is empty
        else:
            #print("Inserted value {} into the linked list".format(val))
            self.head = LinkedListNode(val)
            self.end = self.head

linkedListOne = LinkedList()
linkedListVals = [1,2,3,4,5]
for i in linkedListVals:
    linkedListOne.insert(i)
sol = Solution()
print("Sol {}".format(sol.printLinkedList(sol.oddEvenList(linkedListOne.head))))