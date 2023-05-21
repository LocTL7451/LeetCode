# 1679. Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&id=leetcode-75
""" 
Runtime | 660 ms
Beats | 57.12%
Memory | 29.6 MB
Beats | 8.91%
"""

""" 
    The approach for this problem is very similar to the solution for problem 1. The following is an exerpt of my comments from that problem:
        The approach here is to keep track of the index position of every number in the array as we traverse it
        We know that: 
            Target = Rem + N
            For every number Rem, we know that Rem = Target - N
        Using this information, we can calculate the remainder for every N in our nums array 
        For each N, we calculate Rem and check the hash map to see if we have found the position for that number or not.
        
        The only alterations we make to accomodate the scope of this problem is that we instead store the number of occurances of the current element
        as opposed to storing the element's index position, as we don't need to return the index position of the k sum pairs as we had
        to in problem 1. 
        If we find a match we decrease the number of occurances for the rem in the dictionary and dont store an occurance for the current checked position.
        We also keep a counter and increment it every time a match is found.
"""
class Solution:
    def maxOperations(self, nums, k: int) -> int:
        sumDict = {}
        counter = 0
        
        for j in nums:
            rem = k - j

            if rem in sumDict:
                counter += 1
                sumDict[rem] -= 1
                if sumDict[rem] == 0:
                    sumDict.pop(rem)
            else:
                if j in sumDict:
                    sumDict[j] += 1
                else:
                    sumDict[j] = 1
        return counter
sol = Solution()     
print(sol.maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))