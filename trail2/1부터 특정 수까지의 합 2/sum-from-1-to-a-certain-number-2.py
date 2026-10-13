N = int(input())

def s(n) :
    if n == 1 :
        return 1

    sum = n + s(n-1)
    return sum

print(s(N))