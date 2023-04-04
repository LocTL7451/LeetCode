### 2405. Optimal Partition of String
### https://leetcode.com/problems/optimal-partition-of-string/

"""
Runtime | 131 ms
Beats | 44.59%
Memory | 14.7 MB
Beats | 19.39%
"""

class Solution:
    def partitionString(self, s: str) -> int:
        dict = {}
        solCounter = 1
        for i in range(len(s)):
            #print("Start of for dict: {}".format(dict))
            # Trying to access the current char
            # If char can't be accessed, wipe dict and inc counter else add char to dict 
            try:
                tryVar = dict[s[i]]
                solCounter += 1
                dict = {}
                dict[s[i]] = 1
            except KeyError:                
                dict[s[i]] = 1
        return solCounter
                

sol = Solution()
print(sol.partitionString("abacaba"))