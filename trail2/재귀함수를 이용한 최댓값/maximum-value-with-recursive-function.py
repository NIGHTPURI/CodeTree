n = int(input())
arr = list(map(int, input().split()))

def max_v(n) :
    if n == 1 :
        return arr[0]

    return max(max_v(n-1),arr[n-1])

print(max_v(n))