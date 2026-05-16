n, m = map(int, input().split())

def gcd(a,b) :
    while b != 0 :
        a, b = b, a % b
    return a

def lcm(a,b,c):
    print((a*b)//c)

lcm(n,m,gcd(n,m))
    
# Please write your code here.