# knight problem
# n = 5
# def CorrectPath(x,y,board):
#     if (x >= 0) and (y >=0) and x < n and y < n and board[x][y] == -1:
#         return True
#     return False

# def display(n, board):
#     for i in range(n):
#         for j in range(n):
#             print(f"{board[i][j]} ", end='')
#         print()
    
# def solve(n):
#     board = [[-1 for j in range(n)] for i in range(n)]
    
#     move_x = [2,1,-1,-2,-2,-1,1,2]
#     move_y = [1,2,2,1,-1,-2,-2,-1]
    
#     board[0][0] = 0
    
#     pos = 1
    
#     if (not solveUtil(n,board,0,0,move_x,move_y,pos)):
#         print("Solution not Exist")
#     else:
#         display(n,board)
        
# def solveUtil(n,board,curr_x,curr_y,move_x,move_y,pos):
#     if (pos == n**2):
#         return True
    
#     for i in range(8):
#         new_x = curr_x + move_x[i]
#         new_y = curr_y + move_y[i]
#         if CorrectPath(new_x,new_y,board):
#            board[new_x][new_y] = pos
#            if(solveUtil(n,board,new_x,new_y,move_x,move_y,pos+1)):
#                 return True
#            board[new_x][new_y] = -1
#     return False 

# solve(n)

# kuis rekursif
n,m,a,b,x,y = map(int,input().split())

peta = []
for _ in range (n):
    temp = list(map(int,input().split()))
    peta.append(temp)

ci = a-1
cj = b-1
fi = x-1
fj = y -1
koin = peta[ci][cj]
