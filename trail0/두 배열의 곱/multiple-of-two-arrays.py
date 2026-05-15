b1 = [list(map(int,input().split())) for _ in range(3)]
l = input()
b2 = [list(map(int,input().split())) for _ in range(3)]
for i in range(3):
    for j in range(3):
        print(b1[i][j]*b2[i][j], end=' ')
    print()