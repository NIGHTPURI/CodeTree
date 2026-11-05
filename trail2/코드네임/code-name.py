MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append((codename, int(score)))

print(*min(users,key=lambda x: x[1]))
# Please write your code here.
