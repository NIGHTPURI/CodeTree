n = int(input())
def sq(n) :
    cnt = 1
    for _ in range(n):
        for _ in range(n) :
            print(cnt, end=' ')
            cnt += 1
            if cnt > 9 :
                cnt = 1
        print()

sq(n)
# Please write your code here.