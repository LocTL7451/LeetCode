# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 41 ms
Beats | 28.88%
Memory | 16.4 MB
Beats | 7.63%
"""

"""
    Almost identical approach to problem "#205. Isomorphic Strings"
    Abstract from my explaination in problem 205: 
    
        Cheeky way to map elements to their positions, telling us where the first instance of each character exists. If the character exists earlier
        in one array but later in another, this suggests that the characters are mapped to different key value pairs across both arrays. 
        We then check this pattern to see if the locations are the same, meaning they are mapped in the same spots. 
    The only change from problem 205 to this is that we have a string of substrings (words in the string).
    To make this properly iterable, we simply split the string on blank spaces.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        mappedPatternPositions = []
        mappedSPositions = []
        retFlag = False
        for i in pattern:
            mappedPatternPositions.append(pattern.index(i))
        for j in s:
            mappedSPositions.append(s.index(j))
        print("T Array: {} \nS Array: {}".format(mappedPatternPositions,mappedSPositions))
        if mappedSPositions == mappedPatternPositions:
            retFlag = True  
        return retFlag
sol = Solution()
print(sol.wordPattern("abba", "dog dog dog dog"))
                
 
        
    
