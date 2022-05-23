# Python3으로 제출하면 시간초과가 나옴
# PyPy3으로 제출할 것

import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def check(x1, y1, x2, y2):
    value = a[x1][y1]
    for i in range(x1, x2):
        for j in range(y1, y2):
            if a[i][j] != value:
                return -2
    return value

def count(x1, y1, x2, y2):
    a_total, b_total, c_total = 0, 0, 0
    if check(x1, y1, x2, y2) == -1:
        a_total += 1
    elif check(x1, y1, x2, y2) == 0:
        b_total += 1
    elif check(x1, y1, x2, y2) == 1:
        c_total += 1
    else:
        idxs = [
            [(3 * x1 + 0 * x2) // 3, (3 * y1 + 0 * y2) // 3, (2 * x1 + 1 * x2) // 3, (2 * y1 + 1 * y2) // 3],
            [(2 * x1 + 1 * x2) // 3, (3 * y1 + 0 * y2) // 3, (1 * x1 + 2 * x2) // 3, (2 * y1 + 1 * y2) // 3],
            [(1 * x1 + 2 * x2) // 3, (3 * y1 + 0 * y2) // 3, (0 * x1 + 3 * x2) // 3, (2 * y1 + 1 * y2) // 3],
            [(3 * x1 + 0 * x2) // 3, (2 * y1 + 1 * y2) // 3, (2 * x1 + 1 * x2) // 3, (1 * y1 + 2 * y2) // 3],
            [(2 * x1 + 1 * x2) // 3, (2 * y1 + 1 * y2) // 3, (1 * x1 + 2 * x2) // 3, (1 * y1 + 2 * y2) // 3],
            [(1 * x1 + 2 * x2) // 3, (2 * y1 + 1 * y2) // 3, (0 * x1 + 3 * x2) // 3, (1 * y1 + 2 * y2) // 3],
            [(3 * x1 + 0 * x2) // 3, (1 * y1 + 2 * y2) // 3, (2 * x1 + 1 * x2) // 3, (0 * y1 + 3 * y2) // 3],
            [(2 * x1 + 1 * x2) // 3, (1 * y1 + 2 * y2) // 3, (1 * x1 + 2 * x2) // 3, (0 * y1 + 3 * y2) // 3],
            [(1 * x1 + 2 * x2) // 3, (1 * y1 + 2 * y2) // 3, (0 * x1 + 3 * x2) // 3, (0 * y1 + 3 * y2) // 3],
        ]
        for idx in idxs:
            a, b, c = count(*idx)
            a_total += a
            b_total += b
            c_total += c
    return a_total, b_total, c_total

a, b, c = count(0, 0, n, n)
print(a)
print(b)
print(c)
