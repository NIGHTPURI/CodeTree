n = int(input())

def asec(n) :
    if n == 0 :
        return
    asec(n-1)
    print(n,end=" ")

def desc(n) :
    if n == 0 :
        return
    print(n, end=" ")
    desc(n-1)
    

asec(n)
print()
desc(n)