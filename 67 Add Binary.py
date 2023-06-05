# 67. Add Binary
# https://leetcode.com/problems/add-binary/description/
""" 
Runtime | 52 ms
Beats | 32.23%
Memory | 16.2 MB
Beats | 52.94%
"""

""" 
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        retArr = []
        n = len(a) - 1
        m = len(b) - 1 
    
        while n >= 0 or m >= 0 or carry:    
            if n >=0 :
                carry+=int(a[n])
                n-=1
            if m >=0:
                carry += int(b[m])
                m -= 1
            retArr.append(str(carry%2))
            carry = carry // 2
        retStr = "".join(reversed(retArr))
        return retStr
    
sol = Solution()
print(sol.addBinary("capiTalIze tHe titLe"))