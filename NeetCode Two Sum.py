"""
    Runtime
    27ms
    |
    Beats 100.00%
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
data = [4,5,6]
target = 10
sol = Solution()     
print(sol.twoSum(data,target))