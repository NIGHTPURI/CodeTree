n = int(input())

def hw(n) :
    if n == 0 :
        return
    hw(n-1)
    print('HelloWorld')

hw(n)
# Please write your code here.