# 복습 필요
# 어떤 것으로 시작하는 문자열을 찾으려면 startswith
# for문도 가능하지만 그냥 배열을 하나 더 만들어도 가능

n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

arr = [s for s in str if s.startswith(t)]

arr.sort()


print(arr[k-1])
