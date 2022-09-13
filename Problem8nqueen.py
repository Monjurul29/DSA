print("Enter the number of queens: ", end=" ")
N = int(input())
#NxN matrix with all elements 0
board = [[0 for i in range(N)] for j in range(N)]

def is_attack(i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return 1
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l] == 1:
                    return 1
    return 0

def N_queen(n):
    #if n is 0, solution found
    if n==0:
        return 1
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                #recursion
                #whether we can put the next queen with this arrangment or not
                if N_queen(n-1)==1:
                    return 1
                board[i][j] = 0
    return 0

N_queen(N)
for i in board:
    print (i)
