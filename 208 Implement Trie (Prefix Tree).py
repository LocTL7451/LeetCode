# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&id=leetcode-75

""" 
Runtime | 217 ms
Beats | 21.52%
Memory | 33.9 MB
Beats | 21.85%
"""

""" 

"""
class Trie:
    class TrieNode:
        def __init__(self,char):
            self.char = char
            self.children = {}
            self.endOfAWord = False
            self.counter = 0

    def __init__(self):
        self.root = self.TrieNode(None)

    def insert(self, word: str) -> None:
        currNode = self.root
        for i in range(len(word)):
            
            if word[i] in currNode.children:
                currNode = currNode.children[word[i]]
            else:                
                newTrieNode = self.TrieNode(word[i])
                currNode.children[word[i]] = newTrieNode
                currNode = currNode.children[word[i]]
            currNode.counter += 1
            
        currNode.endOfAWord = True



    def search(self, word: str) -> bool:
        currNode = self.root
        for i in range(len(word)):
            if word[i] in currNode.children:
                currNode = currNode.children[word[i]]
            else:
                return False
        if currNode.endOfAWord:
            return True
        else:
            return False
            

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for i in range(len(prefix)):
            if prefix[i] in currNode.children:
                currNode = currNode.children[prefix[i]]
            else:
                return False
        return True



sol = Trie()     
(sol.insert("Test"))
print(sol.search("Tes"))
print(sol.search("Test"))
print(sol.startsWith("Test"))
