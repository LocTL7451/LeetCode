### 1822. Sign of the Product of an Array
### https://leetcode.com/problems/sign-of-the-product-of-an-array/
"""
Runtime | 68 ms
Beats | 20.12%
Memory | 16.7 MB
Beats | 7.53%
"""
class Solution:
    # Initially misinterpreted the question as asking for a checksum as opposed to product
    def arraySign(self, nums):
        # Set product to 1 for multiplication 
        product = 1
        print(nums)
        for i in range(len(nums)):
            product = product * (nums[i])
        return self.signFunc(product)
    def signFunc(self, product: int) -> int:
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
    
sol = Solution()
print(sol.arraySign([-1,-2,-3,-4,3,2,1]))
