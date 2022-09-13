N = int(input("Enter the number of queen: "))
board = [[0 for i in range(N)] for j in range(N)]
def is_attack(i, j):
    # for row and column
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return 1
    # for diagonal
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
               if board[k][l] == 1:
                   return 1
    return 0

def N_queen(n):
   if n == 0:
       return 1
   for i in range(0, N):
       for j in range(0, N):
           if (not(is_attack(i, j))) and (board[i][j]!= 1):
               board[i][j] = 1
               if N_queen(n - 1) == 1:
                   return 1
               board[i][j] = 0
   return 0


N_queen(N)
for i in board:
    print(i)

