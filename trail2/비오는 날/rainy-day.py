n = int(input())
date = []
day = []
weather = []
data = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

for i in range(n) :
    data.append((date[i],day[i],weather[i]))

data.sort(key=lambda x : x[0])

for d in data :
    if d[2] == "Rain" :
        print(f"{d[0]} {d[1]} {d[2]}")
        break
# Please write your code here.