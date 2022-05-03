n = int(input())
a = [0] + [x[1] for x in sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])]

def locate(x_start_idx, x_end_idx, val):
    if x_start_idx == x_end_idx:
        return x_end_idx
    x_target_idx = (x_start_idx + x_end_idx) // 2
    if x[x_target_idx] == val:
        return x_target_idx
    elif x[x_target_idx] < val:
        return locate(x_target_idx + 1, x_end_idx, val)
    else:
        return locate(x_start_idx, x_target_idx, val)

d = [0]
x = [0]
for i in range(1, n + 1):
    lis_len = locate(0, len(x), a[i])
    if lis_len == len(x):
        x.append(a[i])
    else:
        x[lis_len] = a[i]
    d.append(lis_len)

print(n - max(d))
