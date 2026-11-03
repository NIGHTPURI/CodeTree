n = int(input())
word = [input() for _ in range(n)]

word.sort()
print(*word, sep='\n')
# Please write your code here.