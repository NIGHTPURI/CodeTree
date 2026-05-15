start, end = map(int, input().split())
cnt = 0
for i in range(start, end+1) :
    yak = 0
    for j in range(1,i+1) :
        if i % j == 0 :
            yak +=1
    if yak == 3 :
        cnt += 1
print(cnt)


# Please write your code here.
