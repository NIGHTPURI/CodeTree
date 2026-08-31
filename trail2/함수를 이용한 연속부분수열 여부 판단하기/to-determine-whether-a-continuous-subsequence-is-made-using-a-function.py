n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_true(a,b) :
    for i in range(len(a)-len(b)+1) :
        if a[i:i+len(b)] == b :
            return True
    return False


if is_true(a,b) :
    print('Yes')
else :
    print('No')
# Please write your code here.