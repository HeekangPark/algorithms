n = int(input())
xs = list(map(int, input().split()))
order = {x: i for i, x in enumerate(sorted(set(xs)))}
print(" ".join(map(str, [order[x] for x in xs])))
