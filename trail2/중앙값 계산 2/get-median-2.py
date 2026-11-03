# 복습 필요
# 배열을 중간 중간 끊어서 정렬할땐 슬라이싱 + sorted
n = int(input())
arr = list(map(int, input().split()))
result = []
for i in range(n) :
    if i % 2 == 0 :
        result.append(sorted(arr[:i+1])[i//2])

print(*result)
