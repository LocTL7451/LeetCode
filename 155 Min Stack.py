# 155. Min Stack
# https://leetcode.com/problems/min-stack/?envType=study-plan-v2&id=top-interview-150
"""
Runtime | 75 ms
Beats | 28.47%
Memory | 20.7 MB
Beats | 8%
"""

"""
    The design approach to this question is very simple. We just have a class array "stack" that 
    acts as the stack abstract data type for this class. 
    Given we can index to any position in stack in O(1) time, we can then call append and pops upon the array
    to mirror that of a stack. 

"""

class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        minVal = self.getMin()
        if self.getMin() == None or val < self.getMin():
            minVal = val
        self.stack.append((val, minVal)) 

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return(self.stack[-1][0])

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()