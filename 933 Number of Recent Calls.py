# 933. Number of Recent Calls
# https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 280 ms
Beats | 47.53%
Memory | 21.5 MB
Beats | 57.82%
"""

""" 
    The approach here is to use a queue structure, in which we push each new pinged element to the back of the queue. The queue at any
    given time only contains elements are greater than the current pinged element - 3000. For each element at the front of the queue
    that doesn't match that condition, we simply pop it off the queue, and at the end, return the length of the queue structure.
    This will always work due to the problem statement defining the numbers being pinged as strictly increasing, hence we know that the 
    oldest number in the queue (position 0 or the head of the queue) will always contain the smallest number. 
"""
class RecentCounter:

    def __init__(self):
        self.recentPingArr = []

    def ping(self, t: int) -> int:
        while self.recentPingArr and self.recentPingArr[0] + 3000 < t:
            self.recentPingArr.pop(0)
        self.recentPingArr.append(t)
        return len(self.recentPingArr)

                
           
                
            
            
            

sol = RecentCounter()     
print(sol.ping(1))
print(sol.ping(100))
print(sol.ping(3001))
print(sol.ping(3002))
print(sol.ping(3100))
print(sol.ping(3101))

