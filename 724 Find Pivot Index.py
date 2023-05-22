# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 208 ms
Beats | 24.59%
Memory | 17.8 MB
Beats | 8.85%
"""

""" 
    
"""

class Solution:
    def pivotIndex(self, nums) -> int:
        n = len(nums)
        cumulSummation = 0
        prefixSumArr = []
        for i in range(n):
            cumulSummation += nums[i]
            prefixSumArr.append(cumulSummation)
        print(prefixSumArr)

        for i in range(len(prefixSumArr)):
            print(prefixSumArr[-1] - prefixSumArr[i])
            if i == 0:
                if prefixSumArr[-1] - prefixSumArr[i] == 0:
                    return 0
                
            elif i == len(prefixSumArr) - 1:
                if prefixSumArr[i-1] == 0:
                    return len(prefixSumArr)-1
            elif prefixSumArr[i-1] == prefixSumArr[-1] - prefixSumArr[i]:
                return i 
        
        return -1

sol = Solution()     
print(sol.pivotIndex([0,-1,-1,-1,-1,-1]))