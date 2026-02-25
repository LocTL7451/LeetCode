# the amount of typos i made in this problem made me sad
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return self.checkX(board) and self.checkY(board) and self.checkGroups(board)
    
    def checkX(self, board) -> bool:
        for i in board:
            d = set()
            for j in i:
                if j in d and j != ".":
                    return False
                else:
                    d.add(j)
        return True
    def checkY(self, board):
        for i in range (len(board)):
            d = set()
            for j in range(len(board)):
                if board[j][i] in d and board[j][i] != ".":
                    return False
                else:
                    d.add(board[j][i])
                    
        return True   
    
    # hardcoding cos I cant be bothered right now to do a loop implementation lol
    # might come back around to this once blind 75 done
    def checkGroups(self, board):
        for i in range(len(board)):
            d = set()
            for j in range(3):
                for k in range(3): 
                    r =  (i//3)*3+j 
                    c = (i%3)*3+k 
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in d:
                        return False
                    d.add(board[r][c])                  
        return True
        
        
# data = [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

board=[[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
sol = Solution()     
print(sol.isValidSudoku(board))