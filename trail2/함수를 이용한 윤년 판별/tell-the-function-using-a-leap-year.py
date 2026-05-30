y = int(input())

def year(x) :
    if x % 4 == 0 :
        if x % 100 == 0 and x % 400 != 0 :
            return False
        else :
            return True
    else :
        return False


if year(y) :
    print('true')
else :
    print('false')
# Please write your code here.