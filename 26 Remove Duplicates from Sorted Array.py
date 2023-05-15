### 26. Remove Duplicates from Sorted Array
### https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 160 ms
Beats | 11.55%
Memory | 17.9 MB
Beats | 15.97%

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
                i+=1
            else: 
                nums.pop(i)
                
        print(nums)
        
sol = Solution()
sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
