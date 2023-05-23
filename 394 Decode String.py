# 394. Decode String
# https://leetcode.com/problems/decode-string/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 47 ms
Beats | 23.17%
Memory | 16.3 MB
Beats | 32.81%
"""

""" 
    We have 4 possible elements at any given i position in the string, either a number, a non numeric character, or one of either [ 
    or ].
    This problem would be far easier if it wasn't for the brackets existing. Due to the brackets allowing for nested string duplications, we
    have to make use of the stack and storing the current string and duplication number at any given time.
    We start by keeping track of the number and string. The string storage is standard adding to the current string, but the number
    is a bit harder as we need to put the digit in the correct position. Say for example we have 111, if we take the number verbatim we end up with
    3, as 1+1+1. To solve this, we multiply each current digit by 10 and add the new digit, resulting in 0*10 +1, 1*10+1, 11*10 +1 = 111.
    
    To resolve the brackets, when a new bracket set starts, we store the current string and the current number into the array and wipe the storage
    of the number and string, preparing to parse the positions inside of the current [] set. 
    When we find the closing bracket, we resolve the current bracket by popping the last position in the stack, resulting in the current duplication number 
    for the current string. As we are popping the number first in ] and popping num last in [, we need to ensure that the current string is updated
    with whatever the resolved duplication from the ] in the stack is, so we set the current global string to the stack's previous string and add
    the current string * current num. When we encoutner the next [, this is then pushed onto the stack, starting the process back over again.
"""
class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        string = ''
        stack = []
        for char in s:
            
            if char == "[":
                stack.append(string)
                stack.append(num)
                # Reset string and num for next [] set
                string = ''
                num = 0
            
            elif char == "]":
                
                stackNum = stack.pop()
                stackString = stack.pop()
                string = stackString + stackNum * string
            elif char.isdigit():
                # If a number has digit length of more than 1, we need to multiply the curr dig by 10 to get it to it's required position.
                # An example is 1234, if we just add the digits it becomes 10 instead of 1234, where as if we start with num = 0, then 
                # let num = int(char) + 10 * num, we end up with 1, 10 + 2, 120 + 3, 1230 + 4, which results in 1234 as required.
                num = int(char) + 10 * num 
            
            else:
                string = string + char   
        return string
        

sol = Solution()     
print(sol.decodeString("3[a]2[bc]"))