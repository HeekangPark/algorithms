n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


def check(x1, y1, x2, y2):
    color = a[x1][y1]
    for i in range(x1, x2):
        for j in range(y1, y2):
            if a[i][j] != color:
                return -1
    return color


def count(x1, y1, x2, y2):
    zeros, ones = 0, 0
    if check(x1, y1, x2, y2) == 0:
        zeros += 1
    elif check(x1, y1, x2, y2) == 1:
        ones += 1
    else:
        idxs = [
            [            x1,             y1, (x1 + x2) // 2, (y1 + y2) // 2],
            [(x1 + x2) // 2,             y1,             x2, (y1 + y2) // 2],
            [(x1 + x2) // 2, (y1 + y2) // 2,             x2,             y2],
            [            x1, (y1 + y2) // 2, (x1 + x2) // 2,             y2],
        ]
        for idx in idxs:
            a, b = count(*idx)
            zeros += a
            ones += b

    return zeros, ones


zeros, ones = count(0, 0, n, n)
print(zeros)
print(ones)
