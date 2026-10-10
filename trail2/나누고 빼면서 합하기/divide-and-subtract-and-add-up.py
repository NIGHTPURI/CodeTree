n, m = map(int, input().split())
A = list(map(int, input().split()))


def mod(a) :
    sum = A[a-1]
    while a != 1 :
        if a % 2 == 0 :
            a //= 2
        else :
            a -= 1
        sum += A[a-1]
    return sum
ans = mod(m)
print(ans)

# Please write your code here.