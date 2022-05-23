points = [list(map(int, input().split())) for _ in range(3)]
xs = [p[0] for p in points]
ys = [p[1] for p in points]

missing_x = [x for x in set(xs) if xs.count(x) == 1][0]
missing_y = [y for y in set(ys) if ys.count(y) == 1][0]
print(missing_x, missing_y)