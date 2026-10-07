A = input()

def mod(s) :
    s = set(s)
    if len(s) >= 2 :
        return True
    return False

print('Yes' if mod(A) else 'No')

# Please write your code here.