# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 79 ms
Beats | 24.59%
Memory | 16.3 MB
Beats | 24.61%
"""

"""
    I attempted a stupid approach using stacks and popping based on whether the index was in the first or second half
    but realised the problem is so stupidly easy and achievable using a reversed version of the string of the number
    to check if the number string is a palindrome.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
        
        
"""
    #Stupid stack approach to such a simple problem :<
        stack = []
        x = str(x)
        n = len(x)
        if n == 1:
            return True
        if n%2 == 1:
            flag=True
        else: 
            flag=False
        for i in range(len(x)):
            if flag==True and x[i] == n//2:
                stack.pop(-1)
            elif i in range(n//2):
                stack.append(x[i])
            else:
                if stack[-1] == x[i]:
                    stack.pop(-1)
                    
        if len(stack) == 0:
            return True
        else: 
            return False

"""      

sol = Solution()
print(sol.isPalindrome(1000001))