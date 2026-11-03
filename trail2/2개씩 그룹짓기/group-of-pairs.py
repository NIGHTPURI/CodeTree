n = int(input())
nums = list(map(int, input().split()))

nums.sort()
max_n = 0
for i in range(n) :
    max_n = max(nums[i]+nums[2*n-1-i], max_n)

print(max_n)
# Please write your code here.
