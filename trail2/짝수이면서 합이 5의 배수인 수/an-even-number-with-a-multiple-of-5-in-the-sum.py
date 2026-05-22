n = int(input())

def even_f(x) :
    return n % 2 == 0 and (n//10 + n%10) % 5 == 0

if even_f(n) :
    print('Yes')
else :
    print ('No')

# Please write your code here.