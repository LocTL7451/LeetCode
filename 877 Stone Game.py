# 877. Stone Game
# https://leetcode.com/problems/stone-game/description/

"""
Runtime | 59 ms
Beats | 47.57%
Memory | 16.3 MB
Beats | 48.99%
"""

""" 
    For the O(1) approach, I realised that due to the starting state of piles only ever being even, depending on whether we decide
    to take the front or back, the rest of the actions are decided for us. If we take an even index as out starting point (i=0), we can only
    ever pick from even indexed positions. Vice versa with odd positions. Due to this, we can effectively scan the array and decide which sum is greater
    and hence will always win the game. This is why we simply return True, as due to the nature of piles, we will always win every game.
    
    The DP O(N)^2 solution expands upon this by applying game state theory. In game theory, we give either player a positive or a negative indicator.
    This means that on player 1's turn, they will be trying to maximize the score. On player 2's turn, they will be trying to minimize the score. 
    Knowing this, we can apply an O(1) auxiliary memory solution by calculating which player's turn it is based on two pointers, Left and Right. 
    Left and Right will be slowly incrimented across the array through the use of recursive iteration.
    The program will keep recursing, with each new recursal indicating the start of the other player's turn.
    At the end of execution when left>right, we return 0 and retrace the callbacks back up to the first instance of dp's callback.
    From here, we return to stoneGame a number. If the number is positive, then player 1 has won as player 1 is trying to maximize the dp value.
    If the number is negative, then player 2 has won, as player 2 is trying to minimize the dp value.
"""

#O(N)^2 Solution
class Solution:
    def stoneGame(self, piles) -> bool:
        n = len(piles)
        def dp(left, right):
            if left > right:
                return 0
            # For even number turns
            if (right-left)%2 != 0:
                return max(piles[left]+dp(left+1, right), dp(left, right-1)+piles[right])
            else:
                return min(-piles[left]+dp(left+1, right), dp(left, right-1)-piles[right])
        return dp(0, n -1)>0
"""
# O(1) Solution
class Solution:
    def stoneGameOOne(self, piles) -> bool:
        return True
"""

 
sol = Solution()
sol.stoneGameOOne([5,3,4,5])