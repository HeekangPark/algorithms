# O(n^2) 알고리즘 : top-down

n = int(input())
a = [0] + list(map(int, input().split()))

d = dict()
def f(idx):
    if idx in d:
        return d[idx]

    if idx == 0:
        return 0
    
    d[idx] = max([f(i) for i in range(idx) if a[i] < a[idx]]) + 1
    return d[idx]

print(max([f(i) for i in range(n + 1)]))

# O(n^2) 알고리즘 : bottom-up

n = int(input())
a = [0] + list(map(int, input().split()))

d = [0]
for i in range(1, n + 1):
    d.append(max([d[j] for j in range(i) if a[j] < a[i]]) + 1)

print(max(d))

# O(nlogn) 알고리즘 : bottom-up

n = int(input())
a = [0] + list(map(int, input().split()))

d = [0]
x = [0]

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

for i in range(1, n + 1):
    lis_len = locate(0, len(x), a[i])
    if lis_len == len(x):
        x.append(a[i])
    else:
        x[lis_len] = a[i]
    d.append(lis_len)

print(max(d))