n, m = map(int, input().split())
a = list(map(int, input().split()))

l = list(range(1, n + 1))

move = 0
for item in a:
    loc = l.index(item)
    move += min(loc, len(l) - loc)
    l = l[loc + 1:] + l[:loc]

print(move)

