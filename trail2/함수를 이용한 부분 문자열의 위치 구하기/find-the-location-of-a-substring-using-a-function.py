def is_match(idx):
    for i in range(len(pattern)):
        if text[idx + i] != pattern[i]:
            return False
    return True

text = input()
pattern = input()

ans = -1

for i in range(len(text) - len(pattern) + 1):
    if is_match(i):
        ans = i
        break

print(ans)