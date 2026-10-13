N = int(input())

def sqrt(n) :
    if n < 10 :
        return n*n
    
    return sqrt(n//10) + (n%10)**2

print(sqrt(N))
# Please write your code here.