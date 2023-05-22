# 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 271 ms
Beats | 31.85%
Memory | 17.6 MB
Beats | 57.88%
"""

""" 
    The approach here is to use the python counter class. 
    We first create a set of both word 1 and word 2, creating a list of the unique characters in each list.
    As we can only transform one character into an already existing list, we check to ensure both sets have exactly
    the same set of characters in them. 
    Due to the order of characters not mattering due to the character swap clause, we can solely focus on the quantity of each 
    character in the list. 
    We create a count of all the instances of each character for each list, then create a count of that count, telling us how many
    different groups of character occurances there are. 
    We then check to ensure that both sets have the same number of character occurances as each other, indicating that we can transpose 
    a certain character to another character to fulfil the quantity requirement.
"""
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wordSetOne = set(word1)
        wordSetTwo = set(word2)
        #print("Word 1: {}".format(word1))
        #print("Word 2: {}".format(word2))
        
        n = len(word1)
        m = len(word2)
        mutualOccuranceCount = False

        if wordSetOne == wordSetTwo: 
            #print("Word 1 Counter: {}".format(Counter(word1)))
            #print("Word 2 Counter: {}".format(Counter(word2)))  
            mutualOccuranceCount = Counter(Counter(word1).values()) == Counter(Counter(word2).values())
            #print("Mutual occurance: {}".format(mutualOccuranceCount))
            
        return mutualOccuranceCount
            
        
                 

sol = Solution()     
print(sol.closeStrings("cabbba", "abbccc"))