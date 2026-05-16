n = int(input())
def hab(x) :
    hab = 0
    for i in range(1,x+1) :
        hab += i
    return hab//10
print(hab(n))
# Please write your code here.