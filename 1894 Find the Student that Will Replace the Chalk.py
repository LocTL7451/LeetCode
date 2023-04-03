### 1894. Find the Student that Will Replace the Chalk
### https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
"""
    Runtime | 6649 ms
    Beats | 5.9%
    Memory | 24.2 MB
    Beats | 100%
"""

class Solution(object):
    def chalkReplacer(self, chalk, k):
        if len(chalk) == 1:
            return 0
        temparr = []
        temparr.append(chalk[0])
        for i in range(1,len(chalk)):
            temparr.append(chalk[i] + temparr[-1])
        
        stop = False
        while(stop == False):
            if k < temparr[-1]:
                stop = True
            else:
                k = k - temparr[-1]
        for i in range(len(chalk)):
            if temparr[i] > k:
                return i
        