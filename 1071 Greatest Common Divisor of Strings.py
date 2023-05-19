# 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&id=leetcode-75

"""
Runtime | 40 ms
Beats |67.63%
Memory | 16.2 MB
Beats | 62.12%
"""

"""
    My approach to solving this problem was to use a mathematical GCD value. 
    We first need to verify that a GCD can exist, which is done by checking if s1+s2 is the same as s2+s1. 
    We then find the mathematical GCD between the length of both of the words, and then return the string as
    a splice from the start to the GCD index - 1. 
"""
import math 
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        if str1+str2 == str2+str1:
            gcdVal = math.gcd(n,m)
            return str1[:gcdVal]
        else:
            return ""
             
sol = Solution()
word1 = "LEET"
word2 = "CODE"

print(sol.gcdOfStrings(word1,word2))