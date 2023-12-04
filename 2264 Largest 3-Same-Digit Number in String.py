 ### 2264. Largest 3-Same-Digit Number in String
### https://leetcode.com/problems/largest-3-same-digit-number-in-string/

"""
Runtime | 45 ms
Beats | 44.25%
Memory | 16.2 MB
Beats | 59.27%
"""
import math 
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        last = math.inf 
        largestRet = ""
        counter = 1
        for i in range(len(num)):
            if last == math.inf:
                last = num[i]
            else:
                if last == num[i]:
                    counter += 1
                    if counter == 3:
                        currString = str(last) * 3
                        if largestRet == "":
                            largestRet = currString
                        
                        else:
                            if(int(largestRet) < int(currString)):
                                largestRet = currString
                else:
                    counter = 1
                    last = num[i]
        if largestRet != "":
            return largestRet
        else:
            return ""
        
sol = Solution()
print(sol.largestGoodInteger("6777133339"))