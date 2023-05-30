# 344. Reverse String
# https://leetcode.com/problems/reverse-string/
""" 
Runtime | 788 ms
Beats | 56.52%
Memory | 49.3 MB
Beats | 18.45%
"""

""" 
    The approach here is to use 2 pointers, one at the front and one at the back, slowly moving the pointers inwards and swapping the 
    elements at each pointer.
    
"""

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return s
        left = 0
        right = len(s)-1
        while left <= right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        return s
        
sol = Solution()
print(sol.reverseString(["h","e","l","l","o"]))