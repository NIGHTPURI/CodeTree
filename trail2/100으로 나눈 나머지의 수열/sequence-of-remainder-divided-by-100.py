N = int(input())

def mod(n) :
    if n == 1 :
        return 2
    if n == 2 :
        return 4
    return mod(n-1) * mod(n-2) % 100

print(mod(N))
    
# Please write your code here.