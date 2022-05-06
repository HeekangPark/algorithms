n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]

def check(x1, y1, x2, y2):
    data = a[x1][y1]
    for i in range(x1, x2):
        for j in range(y1, y2):
            if a[i][j] != data:
                return -1
    return data

def compress(x1, y1, x2, y2):
    check_result = check(x1, y1, x2, y2)
    if check_result == 1:
        print(1, end="")
    elif check_result == 0:
        print(0, end="")
    else:
        idxs = [
            [            x1,             y1, (x1 + x2) // 2, (y1 + y2) // 2],
            [            x1, (y1 + y2) // 2, (x1 + x2) // 2,             y2],
            [(x1 + x2) // 2,             y1,             x2, (y1 + y2) // 2],
            [(x1 + x2) // 2, (y1 + y2) // 2,             x2,             y2],
        ]
        print("(", end="")
        for idx in idxs:
            compress(*idx)
        print(")", end="")

compress(0, 0, n, n)
print()