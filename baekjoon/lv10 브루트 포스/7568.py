n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

ranks = [1] * n
for i in range(n):
    for j in range(n):
        if d[j][0] < d[i][0] and d[j][1] < d[i][1]:
            ranks[j] += 1

print(" ".join(map(str, ranks)))