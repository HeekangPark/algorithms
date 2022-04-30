from collections import Counter

word = input().lower()

a = sorted(dict(Counter(list(word))).items(), key=lambda x: x[1], reverse=True)
if len(a) == 1:
    print(a[0][0].upper())
else:
    if a[0][1] == a[1][1]:
        print('?')
    else:
        print(a[0][0].upper())

