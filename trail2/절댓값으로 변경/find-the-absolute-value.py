def mod(arr) :
    for i in range(n) :
        arr[i] = abs(arr[i])



n = int(input())
arr = list(map(int, input().split()))

mod(arr)

for a in arr :
    print(a, end=' ')
# Please write your code here.