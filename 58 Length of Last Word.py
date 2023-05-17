### 58. Length of Last Word
### https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 43 ms
Beats | 26.78%
Memory | 16.4 MB
Beats | 15.79%
"""

"""
    Super simple solution. We split the string into an array upon blank spaces.
    We then just return the length of the last position in the array, which is the last word in the string.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])

sol = Solution()

print(sol.isAnagram("anagram","nagaram"))

        