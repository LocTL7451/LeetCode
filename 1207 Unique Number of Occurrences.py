# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&id=leetcode-75
"""
Runtime
63 ms
Beats
5.78%
Memory
16.4 MB
"""

"""
    The approach here is to loop through arr and use a dictionary to count the number of times
    each element appears in the array.
    We then create a new dictionary and loop through the values of the initial dictionary, using 
    the new dictionary to keep track of unique occurance numbers.
"""

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        elemDict = {}
        occurDict = {}
        for i in arr:
            if i in elemDict: 
                elemDict[i] += 1
            else:
                elemDict[i] = 1
        for i in elemDict.values():
            if i in occurDict:
                return False
            else:
                occurDict[i] = 1
        return True
sol = Solution()
print(sol.uniqueOccurrences([1,2]))

        