### 2300. Successful Pairs of Spells and Potions
### https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

"""
Runtime | 2523 ms
Beats | 5.1%
Memory | 37.2 MB
Beats | 43.80%
"""

"""
[O(nm) approach (TLE)]
    class Solution(object):
        def successfulPairs(self, spells, potions, success):
            
            #:type spells: List[int]
            #:type potions: List[int]
            #:type success: int
            #:rtype: List[int]
            
            solArr = []
            for i in range(len(spells)):
                solArr.append(0)
                for j in range(len(potions)):
                    if spells[i]*potions[j] >= success:
                        solArr[i] += 1
            return solArr
"""
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        print("Spells: {} Potions: {} Success: {}".format(spells, potions, success))
        retArr = []
        # O(log(m)) sort
        potions.sort()
        print("Sorted Potion: {}".format(potions))
        # O(n) iteration
        for i in range(len(spells)):
            #   Number we are checking at a minimum within potions 
            checkNum = success/spells[i]
            print("Check Num: {}/{} = {}".format(success, spells[i], checkNum))
            # Performing binary search for the checknum (O(log(n)) implementation resulting O(n(log(n))) total complexity)
            retArr.append(self.countGreater(potions, checkNum))
        return(retArr)
    
    def countGreater(self,sortedPotions, checkNum):
        potLen = len(sortedPotions)
        leftPointer = 0
        rightPointer = potLen - 1
        leftGreater = potLen
        while (leftPointer <= rightPointer):
            m = int(leftPointer + (rightPointer - leftPointer) / 2)
            print("M: {}".format(m))
            if (sortedPotions[m] >= checkNum):
                leftGreater = m
                rightPointer = m - 1
            else:
                leftPointer = m + 1
        print("Return: {}".format((potLen - leftPointer)))
        return (potLen - leftPointer)
    

            
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
sol = Solution()
print("Solution: {}".format(sol.successfulPairs(spells, potions, success)))