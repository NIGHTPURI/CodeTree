n = int(input())
board = [[0]*n for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if i % 2 == 0 :
            board[j][i] = (j+1)
        else :
            board[j][i] = (n-j)

for i in range(n) :
    for j in range(n) :
        print(board[i][j], end='')
    print()