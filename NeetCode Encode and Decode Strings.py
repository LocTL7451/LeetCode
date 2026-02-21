""" 
    Runtime
    46ms
    |
    Beats 100.00%
"""
class Solution:
    def encode(self, strs: list[str]) -> str:
        s = ""
        for i in strs: 
            s += str(len(i)) + '#' + i
        return s
    def decode(self, s: str) -> list[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            ret.append(s[i:j])
            i = j
        return ret
data = ["Hello","World"]
sol = Solution()     
print(sol.encode(data))
moreData = sol.encode(data)
print(sol.decode(moreData))