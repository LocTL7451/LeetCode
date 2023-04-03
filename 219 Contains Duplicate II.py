### 219. Contains Duplicate II
### https://leetcode.com/problems/contains-duplicate-ii/

"""
    Runtime | 1408 ms
    Beats | 5.3%
    Memory | 27.2 MB
    Beats | 34.64%
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:   
        
        dict = {}
        
        for i, value in enumerate(nums):
            
            if(value in dict) and (i-dict[value] <= k):
            
                return True
            
            dict[value] = i
        
        return False