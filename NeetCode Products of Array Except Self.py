"""
    Runtime
    26ms
    |
    Beats 100.00%
"""
class Solution:
    
    # naive approach cos I'm lazy right now lol
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ret = []
        for i in range(len(nums)):
            ret.append(self.naiveProduct(nums, i))
        return ret
    def naiveProduct(self, nums, current):
        rolling = 1
        for i in range(len(nums)):
            if i != current: 
                rolling *= nums[i]
        return rolling 
data = [-1,0,1,2,3]
sol = Solution()     
print(sol.productExceptSelf(data))