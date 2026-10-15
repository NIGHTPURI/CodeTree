n = int(input())

def mod(n) :
    if n == 1 :
        return 0
    if n % 2 == 0 :
        return mod(n//2) + 1
    else :
        return mod(n*3+1) + 1

print(mod(n))