n, m = map(int, input().split())

def gcd(a,b) :
    while b != 0 :
        a, b = b, a % b
    return a

def lcm(a,b,c):
    print((a//c)*(b//c)*c)

lcm(n,m,gcd(n,m))
    
# Please write your code here.