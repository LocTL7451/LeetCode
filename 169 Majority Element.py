### 169. Majority Element
### https://leetcode.com/problems/majority-element/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 207 ms
Beats | 5.27%
Memory | 17.8 MB
Beats | 28.72%
"""
class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        quantDict = {}
        for i in range(len(nums)):
            if nums[i] in quantDict:
                if quantDict[nums[i]] + 1 > n/2:
                    return nums[i]
                else:
                    quantDict[nums[i]] += 1
            else:
                quantDict[nums[i]] = 1
sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))
