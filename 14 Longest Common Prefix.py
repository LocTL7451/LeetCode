# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 44 ms
Beats | 36.90%
Memory | 16.3 MB
Beats | 21.37%
"""

"""
    The approach here is to make use of an attribute of sorting arrays of strings, which is
    that the greatest difference between strings will be between the first 
    and the last elements of the array.
    To make use of this, we sort the array then compare the first and last elements
    For every matching char, we add the matching char to a return string.
"""
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs = sorted(strs)
        commonPref = ""
        firstWord = strs[0]
        lastWord = strs[-1]
        for i in range(min(len(firstWord),len(lastWord))):
            if firstWord[i] == lastWord[i]:
                commonPref += firstWord[i] 
            else:
                break
        return commonPref

             

sol = Solution()

print(sol.longestCommonPrefix("anagram","nagaram"))

        