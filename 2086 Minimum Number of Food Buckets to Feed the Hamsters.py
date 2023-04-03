### 2086. Minimum Number of Food Buckets to Feed the Hamsters
### https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/description/
"""
    Runtime | 15 ms
    Beats | 100%
    Memory | 15 MB
    Beats | 64.29%
"""

class Solution(object):
    def minimumBuckets(self, hamsters):
        """
        :type hamsters: str
        :rtype: int
        """
        #Base cases 
        if hamsters[0] == 'H' and len(hamsters) == 1:
            return -1
        elif hamsters[:2] == 'HH':
            return -1
        elif hamsters[-2:] == 'HH':
            return -1
        elif 'HHH' in hamsters:
            return -1
        else:
            return (hamsters.count('H') - hamsters.count('H.H'))