# 1268. Search Suggestions System
# https://leetcode.com/problems/search-suggestions-system/description/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 217 ms
Beats | 45.61%
Memory | 23.6 MB
Beats | 19.47%
"""

""" 
    The approach here is to store a list of the first 3 words that are inputted for each Trie character node.
    We then DFS search to the node of each char in the search key and return the contained array at that node.  
"""
class Solution:
    class Trie:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.counter = 0
                self.wordArr = []

        def __init__(self):
            self.root = self.TrieNode()
            self.refNode = self.root

        def insert(self, word: str) -> None:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = self.TrieNode()
                node = node.children[char] 
                if node.counter < 3:
                    node.wordArr.append(word)
                    node.counter += 1


        def searchbByPrefix(self, word: str) -> bool:
            if self.refNode and word in self.refNode.children:
                self.refNode = self.refNode.children[word]
                return self.refNode.wordArr
            else:
                self.refNode = None
                return []
                

    def suggestedProducts(self, products, searchWord: str):
        products.sort()
        self.TrieRef = self.Trie()
        for i in products:
            self.TrieRef.insert(i)
        retArr = []
        for char in searchWord:
            retArr.append(self.TrieRef.searchbByPrefix(char))
        return retArr


sol = Trie()     
(sol.insert("Test"))
print(sol.search("Tes"))
print(sol.search("Test"))
print(sol.startsWith("Test"))
