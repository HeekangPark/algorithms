n = int(input())
for i in range(n):
    a = input()
    score = 0
    cur = 0
    for j in range(len(a)):
        if a[j] == 'O':
            cur += 1
        else:
            cur = 0
        score += cur
    print(score)
