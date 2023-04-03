### 1641. Count Sorted Vowel Strings
"""
    Runtime | 21 ms
    Beats | 40.86%
    Memory | 13.7 MB
    Beats | 15.5%
"""

class Solution(object):

    def countVowelStrings(self, n):
        visited = {}
        def dp(n, numOfLet):
            if numOfLet == 1:
                return numOfLet
            elif n ==  1: 
                return numOfLet
            
            if (n, numOfLet) in visited:
                return visited[n,numOfLet]
            visited[n,numOfLet] = sum(dp(n-1,numOfLet) for numOfLet in range(1, numOfLet + 1))
            return visited[n, numOfLet]
        return dp(n,5)
