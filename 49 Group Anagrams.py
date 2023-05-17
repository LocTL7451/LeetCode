# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 108 ms
Beats | 59.35%
Memory | 20.4 MB
Beats | 20.31%
"""

"""
    The approach here is to use a dictionary and break down each word in strs into it's letter components. We then store 
    the words with the same letter components into the dictionary, with the key being the set of letters the word is 
    made up of and the value being the word itself.
    
    
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        # We use defaultdict as normal dictionary sets in python can't take tuples as keys. 
        dict = defaultdict(list)
        for i in range(len(strs)):
            # Turn every word into the letters that make up the word in alph order
            dict[tuple(sorted(strs[i]))].append(strs[i])
        return list(dict.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))