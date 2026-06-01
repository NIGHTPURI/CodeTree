m1, d1, m2, d2 = map(int, input().split())

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
diff = (sum(month[:m2])+d2) - (sum(month[:m1])+d1)
diff %= 7
print(day[diff])

# Please write your code here.