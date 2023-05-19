# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&id=leetcode-75

"""
Runtime | 102 ms
Beats | 11.4%
Memory | 18 MB
Beats | 10.73%
"""

"""
    The approach here is to make use of two pointers, one starting at the front of the string and one starting at the back
    Due to python strings being immutable objects, we turn the input string into an array which is a mutable object.
    We then iterate through the list moving the pointer towards each other, and check if either pointer is on a vowel
    If both pointers are on vowels, we swap the index position of both of the elements.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        leftPointer = 0
        rightPointer = len(s)-1
        vowelArr = ["a","e","i","o","u","A","E","I","O","U"]
        if len(s) <= 1:
            return s
        sArr = []
        for i in range(len(s)):
            sArr.append(s[i])
        while leftPointer <= rightPointer:
            if sArr[leftPointer] in vowelArr and sArr[rightPointer] in vowelArr:
                sArr[leftPointer],sArr[rightPointer] = sArr[rightPointer],sArr[leftPointer]
                leftPointer += 1
                rightPointer -= 1
            elif sArr[leftPointer] in vowelArr and sArr[rightPointer] not in vowelArr:
                rightPointer -= 1
            elif sArr[leftPointer] not in vowelArr and sArr[rightPointer] in vowelArr:
                leftPointer += 1
            else: 
                leftPointer += 1
                rightPointer -= 1
        return ''.join(sArr)
sol = Solution()
print(sol.reverseVowels("leetcode"))