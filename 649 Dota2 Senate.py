# 649. Dota2 Senate
# https://leetcode.com/problems/dota2-senate/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 192 ms
Beats | 16.25%
Memory | 17.1 MB
Beats | 6.95%
"""

""" 
    The approach here is to make use of a queue to check each enumerated value in the string. 
    The logic here is that if we check position 0 and position 1, assuming the chars are both different, position 0 can choose to cancel
    out position 1's vote, which essentially allows position 0 to have "another round".
    Following this logic, we instantiate two queues, one for each party and loop through the string, enqueuing index positions of 
    either R into R queue or D into D queue. From here, we then loop through both queues and match the index position of each queues current
    index. The smaller value will always win, giving that senator another vote, therefore we enqueue another senator to the queue
    of the party with the smaller value. 
    This process is looped until one party eventually runs out of senators, allowing the remaining party to announce the win. 
"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
                
        class Queue:
            def __init__(self) -> None:
                self.queue = [] 
                self.len = 0
            def enqueue(self,value) -> None:
                self.queue.append(value)
                self.len += 1
            def dequeue(self) -> int:
                self.len -= 1
                return self.queue.pop(0)
            def firstElem(self) -> int:
                return self.queue[0]
            
        n = len(senate)
        radQueue = Queue()
        dirQueue = Queue()
        for index,party in enumerate(senate):
            if party == "R":
                radQueue.enqueue(index)
            else:
                dirQueue.enqueue(index)
        while dirQueue.len >0 and radQueue.len>0:
            if dirQueue.firstElem() > radQueue.firstElem():
                dirQueue.dequeue()
                radQueue.dequeue()
                radQueue.enqueue(n)

                n+=1
            else:
                dirQueue.dequeue()
                radQueue.dequeue()
                dirQueue.enqueue(n)

                n+=1
        if dirQueue.len == 0 and radQueue.len > 0:
            return "Radiant"
        else:
            return "Dire"

            

 
        

sol = Solution()     
print(sol.predictPartyVictory("RD"))