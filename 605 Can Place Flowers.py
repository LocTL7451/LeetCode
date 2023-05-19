# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&id=leetcode-75
"""
Runtime | 210 ms
Beats | 5.13%
Memory | 16.9 MB
Beats | 6.60%
"""

"""
    My approach here is to make as many else if statements until I fill all the required base cases. 
    We first check to make sure the problem is loopable, ie we dont have an empty n or 1 length flowerbed.
    We then check the case where the current index position is the first or last position.
    The big logic section to solve the problem is to check if the current position, the previous position and the next position 
    in the array are all 0, meaning that the flower is placable in i position.
    
    Another valid solution would be checking the len(flowerbed) = 0 or 1 and n != 0 base cases and then 
    checking the first 2 and last 2 positions in flowerbed to see if they are [0,0] denoting a valid flower placement.
    We then search through the rest of the array for [0,0,0] patterns which also denote valid flower placements, saving
    a lot of lines of messy if else code doing so.
    
"""
class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        if n == 0:
            return True
        i = 0
        if len(flowerbed) == 1 and n > 0 and flowerbed[0] != 0:
            return False
        elif len(flowerbed) == 1 and n > 0 and flowerbed[0] != 1:
            return True
        
        while i in range(len(flowerbed)):

            if flowerbed[i] == 0 and i == 0 and flowerbed[i+1] != 1:
                n-=1
                i+=2
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    n-=1
                    break
                else:
                    break
            elif flowerbed[i] == 1:
                i+=1
            elif flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    n-=1
                    i+=2
                else:
                    i+=1
        if n > 0:
            return False
        else:
            return True

        
sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1,0,0],2))