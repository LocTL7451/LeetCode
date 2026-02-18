"""
    Runtime
    28ms
    |
    Beats 100.00%
"""

""" 
    My approach here is to add all of the numbers in the list into a dictionary to form a count of each digit present, with the key being the digit and 
    the value being the number of times it appears in the list. 
    I then sort the dictionary in order of descending value and then return the keys for the first k number of entries.
"""
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for i in nums: 
            if str(i) in d:
                d[str(i)] += 1
            else:
                d[str(i)] = 1
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        firstKValues = list(sorted_dict.keys())[:k]

        return firstKValues 

data = [1,2,2,3,3,3]
sol = Solution()     
print(sol.topKFrequent(data,2))