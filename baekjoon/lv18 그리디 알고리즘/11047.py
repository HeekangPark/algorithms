n, k = map(int, input().split())
cs = sorted([int(input()) for _ in range(n)], reverse=True)
count = 0
for c in cs:
    if k >= c:
        count += k // c
        k = k % c
print(count)
