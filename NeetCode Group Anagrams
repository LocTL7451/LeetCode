class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[str]:
        ret = []
        set = {}
        for i in range(len(strs)): 
            temp = self.createSetString(strs[i])
            if temp in set:
                set[temp].append(i)
            else: 
                set[temp] = [i]
        print(set)
        for j in set:
            ls = [] 
            for k in set[j]:
                ls.append(strs[k])
            ret.append(ls)
        return ret

    def createSetString(self, s: str): 
        set = {}
        for i in s:
            if i in set: 
                set[i] += 1
            else: 
                set[i] = 1
        return ''.join(f"{k}{v}" for k, v in sorted(set.items()))
    
data = ["acta","pots","tops","cat","stop","hat"]
sol = Solution()     
print(sol.groupAnagrams(data))
