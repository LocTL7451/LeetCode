# 1456. Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 163 ms
Beats | 82.32%
Memory | 17.3 MB
Beats | 31.34%
"""

""" 
    Similarly to the approach in problem 643, we initialise the max number of vowels in the subarray by initialising the 
    count of the first window.
    We then subtract 1 from the vowel count if the ith position of the previous window was a vowel, and add 1 to the counter
    if the i+kth position of the current window (next window) is a vowel.
    We then use a max val counter to keep track of the max vowel count throughout the problem and return it at the end.
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n =  len(s)
        vowelDict = {"a","e","i","o","u"}
        if n == 1:
            if s[0] in vowelDict:
                return 1
            else:
                return 0
        maxCount = 0
        for i in range(0, k):
            if s[i] in vowelDict:
                maxCount += 1
        currCount = maxCount
        for i in range(n-k):
            if s[i] in vowelDict:
                currCount -= 1
            if s[i+k] in vowelDict:
                currCount += 1
            maxCount = max(maxCount,currCount)
        return maxCount
            
                     
    

sol = Solution()     
print(sol.maxVowels("leetcode",3))