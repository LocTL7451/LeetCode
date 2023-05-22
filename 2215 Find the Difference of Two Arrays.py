# 2215. Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&id=leetcode-75
""" 
Runtime | 294 ms
Beats | 21.64%
Memory | 33.8 MB
Beats | 9.43%
"""

""" 
    The approach here is to loop through all the numbers in nums1 first and add them to a dictionary. We add the value as the key and the dict
    value as the number 1, indicating that the number is present in arr 1.
    We then loop through nums2, adding each number into the dict, but checking if it already exists with value 1, meaning it overlaps with nums1.
    If they overlap, we change the value to 3 indicating the number overlaps both sets. 
    
    We then just for loop through the dictionary and add all keys with value 1 to return array for nums1, and all keys with values 2 to return 
    array for nums 2.
"""

class Solution:
    def findDifference(self, nums1, nums2):
        diffDict = {}
        retOne = []
        retTwo = []
        for i in nums1:
            diffDict[i] = 1
        for j in nums2:
            if j in diffDict:
                if diffDict[j] == 2:
                    pass
                else:
                    diffDict[j] = 3
            else:
                diffDict[j] = 2
        for k in diffDict:
            if diffDict[k] == 1:
                retOne.append(k)
            elif diffDict[k] == 2:
                retTwo.append(k)
        print(diffDict)
        return [retOne,retTwo]
sol = Solution()     
print(sol.findDifference([-80,-15,-81,-28,-61,63,14,-45,-35,-10],[-1,-40,-44,41,10,-43,69,10,2]))