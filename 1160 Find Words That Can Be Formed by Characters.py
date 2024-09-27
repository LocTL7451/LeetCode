### 1160. Find Words That Can Be Formed by Characters
### https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/?envType=daily-question&envId=2023-12-02

"""
Runtime | 246 ms
Beats | 9.32%
Memory | 16.7 MB
Beats | 96.9%
"""

class Solution:
    def countCharacters(self, words, chars) -> int:
        retCounter = 0

        for word in words:
            dict = {}
            wordLen = len(word) -1
            for i in range(len(chars)):
                if chars[i] in dict:
                    dict[chars[i]] += 1
                else:
                    dict[chars[i]] = 1
            for j in range(len(word)):
                if word[j] in dict and dict[word[j]] > 0:
                    dict[word[j]] -= 1
                else:
                    break 
                if j == wordLen:
                    retCounter += wordLen+1
        return retCounter
    
wordList = ["hello","world","leetcode"]
chars = "welldonehoneyr"
sol = Solution()
print(sol.countCharacters(wordList, chars))

             