n = int(input())
a = sorted(sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0]), key=lambda x: x[1])
count = 1
last_end_time = a[0][1]
for i in range(1, n):
    if a[i][0] < last_end_time:
        continue
    else:
        count += 1
        last_end_time = a[i][1]

print(count)
