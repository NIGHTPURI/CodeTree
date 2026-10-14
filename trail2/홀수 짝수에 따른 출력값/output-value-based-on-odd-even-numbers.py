N = int(input())

def mod(n) :
    if n == 1 :
        return 1
    if n == 2 :
        return 2
    
    return mod(n-2) + n
    
print(mod(N))
