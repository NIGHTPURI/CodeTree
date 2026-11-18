n = int(input())
name = []
korean = []
english = []
math = []

score = []
for _ in range(n):
    name, korean, english, math = input().split()
    score.append((name, int(korean), int(english), int(math)))

score.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for s in score:
    print(s[0], s[1], s[2], s[3])
# Please write your code here.
