fruit = ['apple','banana',"grape", "blueberry", "orange"]
ch = input()
cnt = 0
for s in fruit :
    if s[2] == ch or s[3] == ch :
        print(s)
        cnt += 1
print(cnt)
