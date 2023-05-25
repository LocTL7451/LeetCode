# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/957060420/

""" 
Runtime | 134 ms
Beats | 46.37%
Memory | 16.6 MB
Beats | 24.72%
"""

""" 
    The approach here is to use a dictionary to store the index position of unique values. If a value hasn't been seen before, we add it
    to the dicitonary with key s[i] and set the value to the index position i, otherwise we set the value of the key s[i] to -1, as it is an 
    invalid index. 
    We then loop through all the positions in the dictionary and check for the smallest non -1 value, which we then return as the answer.
"""
import math 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] = -1
            else:
                dict[s[i]] = i
        min = 10**5+1
        for i in dict:
            if dict[i] < min and dict[i] >= 0:
                print(dict[i])
                min = dict[i]

        if min>-1 and min<10**5+1:
            return min
        else:
            return -1

sol = Solution()     
print(sol.firstUniqChar("Testing"))

