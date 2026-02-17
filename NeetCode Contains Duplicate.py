"""
    Runtime
    27ms
    |
    Beats 100.00% 
"""
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        set = {}
        for i in nums:
            if i not in set: 
                set[i] = 1
            else: 
                return True
        return False 
    
data = [1,3,2]
sol = Solution()     
print(sol.hasDuplicate(data))