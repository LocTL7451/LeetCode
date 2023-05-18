# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&id=leetcode-75
"""
Runtime | 199 ms
Beats | 22.8%
Memory | 17.9 MB
Beats | 14.20%
"""

"""
    The approach here is to make use of an attribute of sorting arrays of strings, which is
    that the greatest difference between strings will be between the first 
    and the last elements of the array.
    To make use of this, we sort the array then compare the first and last elements
    For every matching char, we add the matching char to a return string.
"""
class Solution:
    def moveZeroes(self, nums) -> None:
        zeroCounter = 0
        i = 0
        while i in range(len(nums)):
            if nums[i] == 0:
                zeroCounter += 1
                nums.pop(i)
            else:
                i += 1
        for i in range(zeroCounter):
            nums.append(0)
        print(nums)
sol = Solution()

print(sol.moveZeroes([0,1,0,3,12]))

        