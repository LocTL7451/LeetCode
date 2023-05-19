# 443. String Compression
# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&id=leetcode-75

"""
Runtime | 76 ms
Beats | 30.54%
Memory | 16.4 MB
Beats | 18.68%
"""

"""
    The approach to this problem is to use two pointers to iterate through the array with one pointer starting at the start of a 
    char group and one that iterates through, checking how large the char group is. We then replace the chars from the start of the array 
    with the character and the number of occurances. It's slightly confusing, but LeetCode checks chars[:retnum], so we only have to replace 
    the characters in chars from the front and ignore everything behind index position retnum in chars.
"""
class Solution:
    def compress(self, chars) -> int:
        retNum = 0
        i = 0
        n = len(chars)
        while i < n:
            char = chars[i]
            count = 0
            while i < n and chars[i] == char:
                count += 1
                i += 1
            chars[retNum] = char
            retNum += 1
            if count > 1:
                for charac in str(count):
                    chars[retNum] = charac
                    retNum += 1
        print(chars)
        return retNum
        
        
sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c","c"]))