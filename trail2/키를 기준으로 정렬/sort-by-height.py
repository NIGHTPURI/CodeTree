n = int(input())
name = []
height = []
weight = []

p_li = []
class person :
    def __init__(self,n,h,w) :
        self.n = n
        self.h = h
        self.w = w

for i in range(n):
    name, h, w = tuple(input().split())
    p_li.append(person(name,h,w))

p_li.sort(key = lambda x : x.h)

for p in p_li :
    print(p.n, p.h, p.w)



# Please write your code here.