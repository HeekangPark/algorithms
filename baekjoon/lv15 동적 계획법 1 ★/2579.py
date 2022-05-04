n = int(input())
a = [0] + [int(input()) for _ in range(n)]

ans = {}
def f(n, last_step):
    if (n, last_step) in ans:
        return ans[(n, last_step)]

    if n == 1:
        if last_step == 1:
            ans[(n, last_step)] = a[1]
        else:
            ans[(n, last_step)] = 0
    elif n == 2:
        if last_step == 1:
            ans[(n, last_step)] = a[2] + a[1]
        else:
            ans[(n, last_step)] = a[2]
    elif n == 3:
        if last_step == 1:
            ans[(n, last_step)] = a[3] + a[2]
        else:
            ans[(n, last_step)] = a[3] + a[1]
    else:
        if last_step == 1:
            ans[(n, last_step)] = max(f(n - 3, 1), f(n - 3, 2)) + a[n - 1] + a[n]
        else:
            ans[(n, last_step)] = max(f(n - 2, 1), f(n - 2, 2)) + a[n]

    return ans[(n, last_step)]
    
print(max(f(n, 1), f(n, 2)))