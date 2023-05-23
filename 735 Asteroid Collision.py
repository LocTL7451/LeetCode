# 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 113 ms
Beats | 30.33%
Memory | 17.6 MB
Beats | 10.82%
"""

""" 
    The approach here is a bit more complicated that it could be, as we are working from the front of the asteroids array instead of the back as
    I assume most solutions would use (resolving the stack from len(asteroids)-1).
    We append every non negative asteroid whilst iterating through asteroids into the stack. The stack(result) can only contain all positive numbers
    or all negative numbers so we check if the current asteroid, i, is positive which indicates a stack of positive asteroids, otherwise
    if negative indicating a negative stack of asteroids. The +/- state of the stack can change at any given time during the resolution of the
    stack whist iterating through new asteroids.
    The inner logic if the asteroids in stack and current asteroid matches the while statement is very simple. It just checks if the values are the
    same, popping off the current element from the stack as it has matched the new element. It also checks the case where one is greater than the other,
    in which we have to consider the case where an asteroid resolves and the new asteroid is bigger in magnitude than the current stack asteroid. If this
    is the case, we have to pop the current stack element and continue the while loop to resolve the next element, otherwise we break the while as the 
    current asteroid's magnitude is less than the current stack and no changes need to be made.
"""
class Solution:
    def asteroidCollision(self, asteroids):
        astStack = []
        for i in asteroids:
            while len(astStack) and i < 0 and astStack[-1] > 0:
                    if astStack[-1] == -i:
                        astStack.pop()
                        break
                    elif astStack[-1] < -i:
                        astStack.pop()
                            
                        
                    elif astStack[-1] > -i:
                        break
            else: 
                astStack.append(i)
                

        return astStack
        
        
        

""" 
# Misinterpreted the problem statement, so this solution is deprecated.
    n = len(asteroids)
        i = n - 1
        while i >= 1:
            asteroidOne = asteroids[i]
            asteroidTwo = asteroids[i-1]
            
            # Example case: [3,-15,10]
            if asteroidOne > 0 and asteroidTwo < 0:
                if asteroidOne > abs(asteroidTwo):
                    asteroids.pop(i-1)
                    i -= 1
                elif asteroidOne < abs(asteroidTwo):
                    asteroids.pop(i)
                    i -= 1
                else:
                    asteroids.pop(i)
                    i -= 1
                    asteroids.pop(i)
                    i -= 1          
            # Example case: [5,10,-5]
            elif asteroidOne < 0 and asteroidTwo > 0:
                if abs(asteroidOne) > asteroidTwo:
                    asteroids.pop(i-1)
                    i -= 1
                elif abs(asteroidOne) < asteroidTwo:
                    asteroids.pop(i)
                    i -= 1
                else:
                    asteroids.pop(i)
                    i-= 1
                    asteroids.pop(i)
                    i -= 1
            else:
                i -= 2

        return asteroids
        
"""
 
        

sol = Solution()     
print(sol.asteroidCollision([-2,-2,1,-2]))