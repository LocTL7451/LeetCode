### 781. Rabbits in Forest
### https://leetcode.com/problems/rabbits-in-forest/description/?envType=daily-question&envId=2025-04-20

"""
Runtime | 1 ms
Beats | 42.98%
Memory | 18.08 MB
Beats | 29.10%
"""

class Solution:
    def numRabbits(self, answers):
        someMap = {}
        total = 0
        for i in answers:
            # Base case
            # -- We handle when the map position has been reset as well as when 
            # a rabbit discloses that they are the only rabbit in bunch that has the same colour
            if i == 0: 
                total += 1
            else:
                if i not in someMap or i == someMap[i]:
                # -- We have this case to handle over flow for mapping
                    total += i+1
                    someMap[i] = 0
                else:
                    someMap[i] += 1
        return total

input = [10,10,10]
expectedOutput = 11

sol = Solution()
print(sol.numRabbits(input))
if sol.numRabbits(input) != expectedOutput:
    print("Incorrect Solution")