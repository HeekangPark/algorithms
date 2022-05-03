import sys

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cumsum = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        cumsum[i][j] = cumsum[i - 1][j] + cumsum[i][j - 1] - cumsum[i - 1][j - 1] + table[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(cumsum[x2][y2] - cumsum[x1 - 1][y2] - cumsum[x2][y1 - 1] + cumsum[x1 - 1][y1 - 1])
