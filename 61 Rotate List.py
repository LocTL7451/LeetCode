### 61. Rotate List
### https://leetcode.com/problems/rotate-list/description/

"""
Runtime | 229 ms
Beats |44.68%
Memory | 28.1 MB
Beats| 8.64%
"""

"""
    My approach for this solution was slightly inefficient than working soley with linked list logic, but as the runtime ended up working
    out well, I decided to stick with it. We first transform the linked list into an array, which we then rotate by k positions similarly to 
    the rotation performed in problem 189. We then take the rotated array and create a linked list by iterating through each position in the 
    array and creating the list node by node. 
    
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return None
        if not head.next:
            return head
        a = []
        def reverse_array_part(arr, start_index, end_index):
            arr[start_index:end_index+1] = arr[start_index:end_index+1][::-1]

        while head:
            a.append(head.val)
            head = head.next

        n = len(a)
        diffK = k % n
        reverse_array_part(a, 0, n)
        reverse_array_part(a, 0, diffK-1)
        reverse_array_part(a, diffK, n)

        print(a)
        root = ListNode(a[0])
        rootHead = root
        for i in range(1,n):
            root.next = ListNode(a[i])
            root = root.next
        return rootHead
        
sol = Solution()

print(sol.rotate([1,2,3,4,5,6,7], 3))

        