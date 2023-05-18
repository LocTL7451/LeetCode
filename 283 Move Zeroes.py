# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&id=leetcode-75
"""
Runtime | 199 ms
Beats | 22.8%
Memory | 17.9 MB
Beats | 14.20%
"""

"""
    My approach here is to iterate through the nums array and count the number of zeroes
    As we count the zero, we pop the zero from the array.
    Upon completed execution of the iteration, we append zeroes to the end of the array according to the number
    of counted zeroes. 
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

        