# Python3으로 제출하면 시간초과가 나옴
# PyPy3으로 제출할 것

import sys

S = sys.stdin.readline().strip()

d = [[0] * 26 for _ in range(len(S) + 1)]
for i in range(len(S)):
    for c in range(26):
        if c == ord(S[i]) - ord('a'):
            d[i + 1][c] = d[i][c] + 1
        else:
            d[i + 1][c] = d[i][c]

q = int(sys.stdin.readline())
for _ in range(q):
    a, l, r = sys.stdin.readline().strip().split()
    a, l, r = ord(a) - ord('a'), int(l) + 1, int(r) + 1
    print(d[r][a] - d[l - 1][a])