word1 = input()
word2 = input()

wordl1 = list(word1)
wordl2 = list(word2)
wordl1.sort()
wordl2.sort()

if wordl1 == wordl2 :
    print('Yes')
else :
    print('No')
