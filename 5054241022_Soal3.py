#N-Queens
def solveNQueens(n):
 def backtrack(row, cols, diag1, diag2, board):
     if row == n:
         result.append(["".join(row) for row in board])
         return
     
     for col in range(n):
         if col in cols or (row - col) in diag1 or (row + col) in diag2:
             continue
         
         board[row][col] = 'Q'
         cols.add(col)
         diag1.add(row - col)
         diag2.add(row + col)
         
         backtrack(row + 1, cols, diag1, diag2, board)
         
         board[row][col] = '.'
         cols.remove(col)
         diag1.remove(row - col)
         diag2.remove(row + col)
 
 result = []
 board = [['.' for _ in range(n)] for _ in range(n)]
 cols, diag1, diag2 = set(), set(), set()
 
 backtrack(0, cols, diag1, diag2, board)
 
 return result

print(solveNQueens(4))
