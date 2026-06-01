a, b, c = map(int, input().split())

start = (11*24*60)+(11*60)+11

print((a*24*60+b*60+c)-start if (a*24*60+b*60+c)-start >= 0 else -1)
# Please write your code here.