n = int(input())
arr = list(map(int, input().split()))
def gcd(a,b) :
    while b > 0 :
        a, b = b, a % b
    return a


def mod(n):
    if n == 1:
        return arr[0]

    prev = mod(n-1)
    return arr[n-1] * prev // gcd(arr[n-1], prev)

print(mod(n))