### 881. Boats to Save People
### https://leetcode.com/problems/boats-to-save-people/

"""
Runtime | 1255 ms
Beats | 5.31%
Memory | 19 MB
Beats | 10.18%
"""

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
            people[i] is the weight of the i-th person 
            limit is the weight limit of each boat 
        """ 
        sortedPeople = sorted(people, reverse=True)
        # Sorts array in descending order 
        print(sortedPeople)
        forwardPointer = 0
        backwardPointer = len(sortedPeople) - 1
        solCounter = 0
        print("DEBUG {} FORWARD {} BACKWARD {}".format(solCounter, forwardPointer, backwardPointer))
        
        while forwardPointer <= backwardPointer:
            print("Entered While")
            print("DEBUG {} FORWARD {} BACKWARD {}".format(solCounter, forwardPointer, backwardPointer))
            if sortedPeople[forwardPointer] == limit:
                print("Entered IF 1")
                solCounter += 1
                forwardPointer += 1
            elif forwardPointer == backwardPointer:
                print("Entered IF 2")
                solCounter += 1
                break
            elif sortedPeople[forwardPointer] + sortedPeople[backwardPointer] <= limit:
                print("Entered IF 3")                
                forwardPointer += 1
                backwardPointer -= 1
                solCounter += 1
            else:
                solCounter += 1
                forwardPointer += 1
        return solCounter
        
    
sol = Solution()
print(sol.numRescueBoats([3,5,3,4],5))
#[5,4,3,3]