### 27. Remove Element
### https://leetcode.com/problems/remove-element/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 51 ms
Beats | 15.44%
Memory | 16.2 MB
Beats | 31.38%
"""
class Solution:
    def removeElement(self, nums, val):
        backIterator = len(nums) - 1
        k = 0
        i = 0
        while i <= len(nums)-1:
            if nums[i] != val:
                k += 1
                i+=1
            else: 
                nums[i],nums[backIterator] = nums[backIterator], "_"
                backIterator -= 1
                nums.pop(-1)
                
        print(nums)
        
sol = Solution()
sol.removeElement([3,2,2,3],3)
