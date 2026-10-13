N = int(input())

def a(n) :
    if n == 0 : 
        return
    print(n, end = " ")
    a(n-1)
    print(n, end = " ")

a(N)
# Please write your code here.