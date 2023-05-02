### 1491. Average Salary Excluding the Minimum and Maximum Salary
### https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""
Runtime | 45 ms
Beats | 5.34%
Memory | 16.4 MB
Beats | 5.29%
"""
class Solution:
    def average(self, salary):
        salary.sort()
        print(salary)
        avgSum = 0
        for i in range(1,len(salary)-1):
            print(salary[i])
            avgSum += salary[i]
        return(avgSum/(len(salary)-2))
    
sol = Solution()

print(sol.average([4000,3000,1000,2000]))