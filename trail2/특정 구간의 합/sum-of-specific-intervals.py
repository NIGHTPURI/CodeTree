n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

def sum(m):
    for i in range(m) :
        sum = 0
        a = queries[i][0]
        b = queries[i][1]
        for j in range(a-1,b) :
            sum += arr[j]
        print(sum)

sum(m)
# Please write your code here.