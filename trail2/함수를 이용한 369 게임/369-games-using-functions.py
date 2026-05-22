a, b = map(int, input().split())

def tsn(x) :
    while x > 0 :
        if x % 10 == 3 or x % 10 == 6 or x % 10 == 9 :
            return True
        else :
            x //= 10
    return False

def three(x) :
    cnt = 0
    while x > 0 :
        cnt += (x%10)
        x //= 10
    return cnt%3 == 0

cnt = 0
for i in range(a,b+1):
    if tsn(i) or three(i) :
       cnt += 1

print(cnt) 
# Please write your code here.