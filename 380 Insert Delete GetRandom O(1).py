# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 47 ms
Beats | 51.90%
Memory | 16.6 MB
Beats | 21.16%
"""

"""
    The design approach for this question is using a dictionary to store the set of the class
    This ensures that at any given time, we can check if a value already exists within the set. 
    Usually, the "in" keyword reserves a time complexity of at least O(N), which violates the complexity requirement of the problem
    Due to the usage of a hash table, the "in" keyword actually only uses O(1) complexity, as the __contains__ in hash table's 
    built in functions is an O(1) operation, mapping the abstracted function to the "in" keyword. 
    
    To handle the  randomness of the program, we make use of the Random python library, specifically the RandRange function, which allows us to 
    define a range of values for the function to select a value from. 
    We then take that random selected value and return the value at the index position of the class's set. 
"""
import random as r
class RandomizedSet:

    def __init__(self):
        self.duplicateDict = {}

    def insert(self, val: int) -> bool:
        if val in self.duplicateDict:
            return False
        else:
            self.duplicateDict[val] = 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.duplicateDict:
            del self.duplicateDict[val]
            return True
        else:
            return False
    def getRandom(self) -> int:
        numElem = len(self.duplicateDict)
        randPos = r.randrange(0,numElem)
        return list(self.duplicateDict)[randPos]
    def printSet(self):
        print(list(self.duplicateDict))


"""
# Driver code for the problem
sol = RandomizedSet()
sol.insert(1)
sol.printSet()
sol.remove(2)               
sol.printSet()
sol.insert(2)
sol.printSet()
sol.remove(2)
sol.printSet()
sol.insert(2)
sol.insert(3)
sol.printSet()
print(sol.getRandom())
            
"""         

        
    
