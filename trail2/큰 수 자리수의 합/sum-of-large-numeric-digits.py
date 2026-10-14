a, b, c = map(int, input().split())

n = a*b*c

def mod(n) :
    if n < 10 :
        return n
    return mod(n//10) + n%10

print(mod(n))
# Please write your code here.