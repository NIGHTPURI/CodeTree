n = int(input())
h = 0
cnt = 1
while h < n :
    h += cnt
    if h >= n :
        break
    cnt += 1
print(cnt) 