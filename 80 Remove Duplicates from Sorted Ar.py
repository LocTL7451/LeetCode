### 80. Remove Duplicates from Sorted Array II
### https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 75 ms
Beats | 15.62%
Memory | 16.3 MB
Beats | 38.97%
"""
class Solution:
    def removeDuplicates(self, nums):
        k = 0
        i = 0
        copyDict = {}
        while i <= len(nums)-1:
            if nums[i] not in copyDict:
                copyDict[nums[i]] = 1
                k += 1
                i += 1
            elif copyDict[nums[i]] == 1:
                copyDict[nums[i]] += 1
                k += 1
                i += 1
            else: 
                nums.pop(i)
        
sol = Solution()
sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
