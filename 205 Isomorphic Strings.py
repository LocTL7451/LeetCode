# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 71 ms
Beats | 8.45%
Memory | 17.1 MB
Beats | 5.42%
"""

""" 
    Cheeky way to map elements to their positions, telling us where the first instance of each character exists. If the character exists earlier
    in one array but later in another, this suggests that the characters are mapped to different key value pairs across both arrays. 
    We then check this pattern to see if the locations are the same, meaning they are mapped in the same spots. 
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappedSPositions = []
        mappedTPositions = []
        retFlag = False
        for i in s:
            mappedSPositions.append(s.index(i))
        for j in t:
            mappedTPositions.append(t.index(j))
        print("T Array: {} \nS Array: {}".format(mappedTPositions,mappedSPositions))
        if mappedSPositions == mappedTPositions:
            retFlag = True  
        return retFlag
        """
            mappedDictS = {}
            mappedDictT = {}
            matchFlag = False
            for i in range(len(s)):
                if s[i] == t[i]:
                    if s[i] in mappedDictS:
                        matchFlag = True
                    else:
                        mappedDictS[s[i]] = t[i]
                        matchFlag = True
                else:
                    if s[i] in mappedDictS:
                        if mappedDictS[s[i]] == t[i]:
                            matchFlag = True
                        else:
                            matchFlag = False
                            break
                    else:
                        mappedDictS[s[i]] = t[i]
                        matchFlag = True
                        
            return matchFlag
        """
sol = Solution()
print(sol.isIsomorphic("babq", "babc"))
                
 
        
    
