n = int(input())
ans = 1
for i in range(1,n+1):
    for _ in range(i) :
        print(ans, end = ' ')
        ans += 1
    print()

        