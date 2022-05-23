import sys

n, M = map(int, sys.stdin.readline().split())
a = list(map(int, input().split()))

cumsum = [0] * (n + 1)
for i in range(1, n + 1):
    cumsum[i] = cumsum[i - 1] + a[i - 1]

for m in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(cumsum[j] - cumsum[i - 1])