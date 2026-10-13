N = int(input())


def p(n) :
    if n == 1 :
        return 1
    if n == 2 :
        return 1
    
    return p(n-1) + p(n-2)

print(p(N))
# Please write your code here.