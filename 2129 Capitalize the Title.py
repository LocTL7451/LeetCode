# 2129. Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title/

""" 
Runtime | 49 ms
Beats | 27.64%
Memory | 16.7 MB
Beats | 8.41%
"""

""" 
    The approach here is divide n by 5 until you can't, then by 3 then by 2, resulting in 1 or not 1 if n has another prime factor. 
"""

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        a = title.split(" ")
        for i in range(len(a)):
            a[i] = a[i].lower()
            print(a[i])
            if len(a[i]) > 2:
                print("temp")
                a[i] = a[i].capitalize()
        return " ".join(a)
sol = Solution()
print(sol.capitalizeTitle("capiTalIze tHe titLe"))