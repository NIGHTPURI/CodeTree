n = int(input())
nums = list(map(int, input().split()))

nums.sort()
print(*nums)
nums = nums[::-1]
print(*nums)


# Please write your code here.
