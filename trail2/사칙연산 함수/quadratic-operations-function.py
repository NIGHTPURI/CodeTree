a, o, c = input().split()
a = int(a)
c = int(c)
def plus(x,y) :
    return x+y

def minus(x,y) :
    return x-y

def mul(x,y) :
    return x*y

def div(x,y) :
    return x//y

if o == '+' :
    print(f'{a} {o} {c} = {plus(a,c)}')
elif o == '-' :
    print(f'{a} {o} {c} = {minus(a,c)}')
elif o == '*' :
    print(f'{a} {o} {c} = {mul(a,c)}')
elif o == '/' :
    print(f'{a} {o} {c} = {div(a,c)}')
else :
    print('False')
# Please write your code here.