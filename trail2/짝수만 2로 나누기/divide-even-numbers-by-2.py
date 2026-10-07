n = int(input())
arr = list(map(int, input().split()))


def mod(arr) :
    for i in range(n):
        if arr[i] % 2 == 0 :
            arr[i] //= 2


mod(arr)

for a in arr :
    print(a, end=' ')
# Please write your code here.