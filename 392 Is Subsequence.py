# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&id=leetcode-75

"""
Runtime | 56 ms
Beats | 7.57%
Memory | 16.4 MB
Beats | 21.66%
"""

"""
    We keep 2 pointers, 1 in range of s and one looping through t while neither pointer is out of range of the respective strings.
    We just loop through and check at the end of the while loop if the pointer position for s is pointing to the end of s, which
    indicates that the loop has matched all instances of s in order from t. 
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tLen = len(t)
        sLen = len(s)
        if sLen > tLen:
            return False
        sPointer = 0
        i = 0
        while sPointer!=sLen and i != tLen:
            if t[i] == s[sPointer]:
                sPointer += 1
                i += 1
            else:
                i += 1
        if sPointer == sLen:
            return True
        else: 
            return False
        
                
        
        
sol = Solution()
print(sol.isSubsequence("axc","ahbgdc"))