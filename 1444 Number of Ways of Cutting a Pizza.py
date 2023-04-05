### 1444. Number of Ways of Cutting a Pizza
### https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/
    
"""
Runtime | 236 ms
Beats | 56.12%
Memory | 16 MB
Beats | 33.47%
"""

class Solution:
    def ways(self, pizza, k):
        # New approach to dp that doesn't require calculation at every step
        # Instead attempts to calculate the number of apples in any given (numRows,numCols) to (endRow,endCol) sub section
        # This is because by mapping out the current state of each cut, we can see overlapping sub problems that are found across the states
        # Suggesting that this is the proper implementation of a DP solution for maximal reduction.
        self.numRows = len(pizza)
        self.numCols = len(pizza[0]) 
        self.mod = 10 ** 9 + 7
        self.calcSum = [[0] * (self.numCols + 1) for _ in range(self.numRows + 1)]
        #print(calcSum)
        
        for endRow in range(self.numRows - 1, -1, -1):
            for endCol in range(self.numCols - 1, -1, -1):
                self.calcSum[endRow][endCol] = self.calcSum[endRow][endCol + 1] + self.calcSum[endRow + 1][endCol] - self.calcSum[endRow + 1][endCol + 1] + (pizza[endRow][endCol] == 'A')
        #print(calcSum)

        def dynamic(k, refRow, refCol):
            # Base case that catches the instance where no apples in the area
            if self.calcSum[refRow][refCol] == 0:
                return 0
            # Catching the 0 apple in area above allows us to assume that there is at least one apple in this cut
            # Therefore if there is 1 cut remaining, we can simply return 1
            elif k == 0:
                return 1
            sol = 0
            # Iterating through all possible horizontal cuts at each given pizza state array assuming a valid apple placement
            for newRow in range(refRow+1,self.numRows):
                if self.calcSum[refRow][refCol] - self.calcSum[newRow][refCol] > 0:
                    sol = (sol + dynamic(k - 1, newRow, refCol)) % self.mod 
            # Iterating through all possible vertical cuts at each given pizza state array assuming a valid apple placement
            for newCol in range(refCol+1,self.numCols):
                if self.calcSum[refRow][refCol] - self.calcSum[refRow][newCol] > 0:
                    sol = (sol + dynamic(k - 1, refRow, newCol)) % self.mod 
            return sol
        return dynamic(k-1,0,0)
        
        
        """
        ### Deprecated attempt at storing graph states and manually calculating slices
        self.pizza = pizza 
        self.k = k 
        solCounter = 0
        # Given a pizza state indicated by pizStart (Array coords of top left) and pizEnd (Array coords of bottom right)
        # Store the resulting cut given by a cutAfter index position into the array to avoid recalculating list splice each cut  
        self.memoDictHor = {}
        # For each entry in the memoDictHor dictionary:
        # (pizStart, pizEnd) => (pizStateTop, pizStateBot) => 
        # pizStateTop => (pizStart, pizEnd, hasApple) | 
        # pizStateBot => (pizStart, pizEnd, hasApple) => 
        # pizStart => (x,y) | 
        # pizEnd => (x,y) |
        # hasApple => True || False        
        self.memoDictVert = {}
        # For each entry in the memoDictVert dictionary: 
        # (pizStart, pizEnd) => (pizStateLeft, pizStateRight) => 
        # pizStateLeft => (pizStart, pizEnd, hasApple) || 
        # pizStateRight => (pizStart, pizEnd, hasApple)
        # pizStart => (x,y) | 
        # pizEnd => (x,y) |
        # hasApple => True || False   
        
        #return(solCounter % (10^9 + 7))
        self.pizzaStart = (0,0)
        self.pizzaEnd = (len(self.pizza) - 1 , len(self.pizza[0]) - 1)
        
        horRet = self.cutHorizontal(self.pizzaStart, self.pizzaEnd, cutAfterRowIndex=0)
        print(self.memoDictHor)
        #print(self.pizza[horRet[0][0][0]:horRet[0][1][0]][horRet[0]])
    def cutHorizontal(self, pizStart, pizEnd, cutAfterRowIndex):
        try:
            return(self.memoDictHor[(pizStart,pizEnd)])
        except KeyError:  
            self.memoDictHor[(pizStart,pizEnd)] = ((pizStart,(cutAfterRowIndex, pizEnd[1]), self.hasApple(pizStart,(cutAfterRowIndex, pizEnd[1]))), ((cutAfterRowIndex + 1, pizStart[1]), pizEnd, self.hasApple(cutAfterRowIndex + 1, pizStart[1]), pizEnd))

            return (self.memoDictHor[(pizStart,pizEnd)])
            
    def cutVertical(self, pizStart, pizEnd, cutAfterColIndex):
        try:
            return(self.memoDictVert[(pizStart,pizEnd)])
        except KeyError:  
            self.memoDictVert[(pizStart,pizEnd)] = ( (pizStart, (pizEnd[0], cutAfterColIndex) , self.hasApple(pizStart, (pizEnd[0], cutAfterColIndex)) ), ( (cutAfterColIndex+1,pizStart[0]) , pizEnd , self.hasApple((cutAfterColIndex+1,pizStart[0]) , pizEnd) ) )
            return self.memoDictVert[(pizStart,pizEnd)]
    
    def hasApple(self, pizStart, pizEnd):
        for row in range(pizStart[0], pizEnd[0] + 1):
            for col in range(pizStart[1], pizEnd[1] + 1):
                if self.pizza[row][col] == "A":
                    return True
        return False
        """
pizza = ["A..","A..","..."]
k = 1
sol = Solution()
print(sol.ways(pizza,k))
        
    