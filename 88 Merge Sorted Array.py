### 88. Merge Sorted Array
### https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&id=top-interview-150

"""
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            nums1[m+i] = nums2[i]
        nums1.sort()
        
        
sol = Solution()

print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))

        