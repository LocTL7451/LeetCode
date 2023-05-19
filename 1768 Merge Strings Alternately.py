# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&id=leetcode-75

"""
Runtime | 52 ms
Beats | 5.65%
Memory | 16.3 MB
Beats | 11.93%
"""

"""
    My approach to solving this question was to use the smaller word's length as the iteration upper range, looping through 
    all positions of both words up until the upper range and adding them in alternating order to the solution string.
    From here, we then add the rest of which ever word is bigger or nothing in the case where both words are of the 
    same length. 
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        
        iterationLen = min(n,m)
        solString = ""
        for i in range(iterationLen):
            solString += word1[i]
            solString += word2[i]
        print(solString)
        if n>m:
            for i in range(m,n):
                solString += word1[i]
        elif m>n:
            for i in range(n,m):
                solString += word2[i]
        return solString   
sol = Solution()
word1 = "abcd"
word2 = "pq"
print(sol.mergeAlternately(word1,word2))