# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&id=leetcode-75

"""
Runtime | 49 ms
Beats | 13.46%
Memory | 16.3 MB
Beats | 8.90%
"""

"""
    My approach is to sweep the array and check what the max val is initially.
    We then loop through the array and add extraCandies to each position, if the position is greater
    than the max val, then we swap the position to True otherwise False.
"""
class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        maxCandies = max(candies) 
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxCandies:
                candies[i] = True
            else:
                candies[i] = False
        return candies
        
sol = Solution()


print(sol.kidsWithCandies([12,1,12],11))