n = int(input())
num = list(map(int, input().split()))
square = [i**2 for i in num]
print(' '.join(map(str,square)))