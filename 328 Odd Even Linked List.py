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
        #[1,2,4,6,7,9]
        if head.val % 2 == 0:
            prevStepper = None
            stepper = head
            while stepper and stepper.val %2 == 0:
                prevStepper = stepper
                stepper = stepper.next
            if stepper:
                stepper.next = prevStepper
                prevStepper.next = stepper.next
                head = stepper 
            else: 
                return head

        currNode = head
        stepper = currNode
        prevNode = stepper
        while currNode:
            if currNode.val % 2 == 1:
                prevNode = currNode
                currNode = currNode.next
                stepper = currNode
            else:
                while stepper and stepper.val % 2 == 0:
                    stepper = stepper.next
                if not stepper:
                    return head
                else:
                    #[1,2,3,4,5]
                    temp = stepper.next #4
                    prevNode.next = stepper
                    stepper.next = currNode
                    stepper.next.next = temp
                    currNode = stepper
                    self.printLinkedList(head)
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