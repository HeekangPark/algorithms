w1, w2 = [input() for _ in range(2)]

d = [[0] * (len(w2) + 1) for _ in range(len(w1) + 1)]

w1, w2 = " " + w1, " " + w2

for i in range(1, len(w1)):
    for j in range(1, len(w2)):
        if w1[i] == w2[j]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(max([max(row) for row in d]))