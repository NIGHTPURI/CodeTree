nums = [int(input()) for _ in range(10)]
t = 0
f = 0
for i in nums :
    if i % 3 == 0 :
        t += 1
    if i % 5 == 0 :
        f += 1
print(t,f)