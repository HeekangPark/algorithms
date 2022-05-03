n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
ws = [0] + [x[0] for x in items]
vs = [0] + [x[1] for x in items]

d = [[0] * (k + 1) for _ in range(n + 1)]
for item_idx in range(1, n + 1):
    for w in range(1, k + 1):
        if ws[item_idx] <= w:
            d[item_idx][w] = max(d[item_idx - 1][w], d[item_idx - 1][w - ws[item_idx]] + vs[item_idx])
        else:
            d[item_idx][w] = d[item_idx - 1][w]

print(d[n][k])
    