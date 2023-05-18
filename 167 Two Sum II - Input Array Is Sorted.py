# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&id=top-interview-150
""" 
Runtime | 137 ms
Beats | 41.69%
Memory | 17.1 MB
Beats | 36.7%
"""

""" 
    The approach here is to keep track of the index position of every number in the array as we traverse it
    We know that: 
        Target = Rem + N
        For every number Rem, we know that Rem = Target - N
    Using this information, we can calculate the remainder for every N in our nums array 
    For each N, we calculate Rem and check the hash map to see if we have found the position for that number or not 
"""

class Solution:
    def twoSum(self, numbers, target: int):
        sumDict = {}
        for i, j in enumerate(numbers):
            rem = target - j
            if rem in sumDict:
                return [sumDict[rem] + 1, i + 1]
            else:
                sumDict[j] = i
sol = Solution()     
print(sol.twoSum([2,7,11,15], 9))