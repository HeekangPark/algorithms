n, m = map(int, input().split())
board = [[(1 if x == "W" else 0) for x in input()] for _ in range(n)]

answers = []
answers.append([
    [0, 1] * 4,
    [1, 0] * 4,
    [0, 1] * 4,
    [1, 0] * 4,
    [0, 1] * 4,
    [1, 0] * 4,
    [0, 1] * 4,
    [1, 0] * 4,
])
answers.append([
    [1, 0] * 4,
    [0, 1] * 4,
    [1, 0] * 4,
    [0, 1] * 4,
    [1, 0] * 4,
    [0, 1] * 4,
    [1, 0] * 4,
    [0, 1] * 4
])

min_recolor = 64

for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        for answer in answers:
            count = 0
            for a in range(8):
                for b in range(8):
                    if answer[a][b] != board[i + a][j + b]:
                        count += 1

            if count < min_recolor:
                min_recolor = count

print(min_recolor)