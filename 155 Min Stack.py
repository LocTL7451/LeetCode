# 155. Min Stack
# https://leetcode.com/problems/min-stack/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 557 ms
Beats | 10.64%
Memory | 20.2 MB
Beats | 31.43%
"""

"""
    The design approach to this question is very simple. We just have a class array "stack" that 
    acts as the stack abstract data type for this class. 
    Given we can index to any position in stack in O(1) time, we can then call append and pops upon the array
    to mirror that of a stack. 
    
    I realise there is a more efficient way of keeping track of the min which would be to continuously keep track
    of the min at any given time, but this was just an easier way out.  
"""

import math
class MinStack:

    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return(self.stack[-1])

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()