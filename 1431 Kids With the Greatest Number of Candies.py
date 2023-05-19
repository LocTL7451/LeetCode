# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&id=leetcode-75

"""
Runtime | 49 ms
Beats | 13.46%
Memory | 16.3 MB
Beats | 8.90%
"""

"""
    My approach to solving this problem was to use a mathematical GCD value. 
    We first need to verify that a GCD can exist, which is done by checking if s1+s2 is the same as s2+s1. 
    We then find the mathematical GCD between the length of both of the words, and then return the string as
    a splice from the start to the GCD index - 1. 
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