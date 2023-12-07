### 1688. Count of Matches in Tournament
### https://leetcode.com/problems/count-of-matches-in-tournament/?envType=daily-question&envId=2023-12-05
"""
Runtime | 40 ms
Beats | 41.25%
Memory | 16.4 MB
Beats | 22.47%
"""

# For any given round, we have n//2 number of fights, with n//2 + remainder if it exists teams moving to next round. 
# With this, we can loop through until there are only 2 teams left, meaning there will be 1 fight left, so we return the counter number + 1 taking into acccount the last fight.
class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n < 2:
            return 0
        matchCounter = 0
        while n > 2:
            matchCounter += (n//2)
            n = n//2 + (n%2)
        return matchCounter+1

sol = Solution()
print(sol.numberOfMatches(14))