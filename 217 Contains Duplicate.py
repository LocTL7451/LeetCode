# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/
""" 
Runtime | 590 ms
Beats | 13.99%
Memory | 34.5 MB
Beats | 6.19%
"""

class Solution:
    def containsDuplicate(self, nums) -> bool:
        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 1
        return False


sol = Solution()
print(sol)