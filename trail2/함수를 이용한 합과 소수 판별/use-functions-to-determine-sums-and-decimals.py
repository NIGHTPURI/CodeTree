a, b = map(int, input().split())
cnt = 0
def is_prime(x) :
    if x < 2 :
        return False
    
    for i in range(2, int(x**0.5)+1) :
        if x%i == 0 :
            return False
    return True
    
def is_even(x) :
    return sum(map(int, str(x))) % 2 == 0

for i in range(a,b+1) :
    if is_prime(i) and is_even(i) :
        cnt += 1

print(cnt)

