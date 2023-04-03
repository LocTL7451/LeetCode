### 1662. Check If Two String Arrays are Equivalent
### https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/

"""
    Runtime | 70 ms
    Beats | 5.23%
    Memory | 13.9 MB
    Beats | 22.6%
"""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wordOne = ""
        wordTwo = ""
        for i in word1:
            wordOne += i
        for i in word2:
            wordTwo += i
        if wordOne == wordTwo:
            return True
        else:
            return False