### 1716. Calculate Money in Leetcode Bank
### https://leetcode.com/problems/calculate-money-in-leetcode-bank/?envType=daily-question&envId=2023-12-06
"""
Runtime | 41 ms
Beats | 48.52%
Memory | 16.2 MB
Beats | 40.52%
"""

# Essentially breaking down n into the number of weeks (groups of 7) and the days left over.
# Each full week, $7 is added to the value of the last week and added to the total, meaning we multiply i (current week number) by 7 and add it to 28 (7!)
# We then break down the number of remaining days which is the number of weeks +1 (starting value) and add j (current day number) to each iteration
class Solution:
    def totalMoney(self, n: int) -> int:
        counter = 0
        numOfWeeks = n // 7
        remDays = n % 7
        for i in range(numOfWeeks):
            counter += (28 + (i * 7))
        if remDays > 0:
            for j in range(remDays):
                counter += (numOfWeeks + 1 + j)
        return counter
sol = Solution()
print(sol.totalMoney(10))