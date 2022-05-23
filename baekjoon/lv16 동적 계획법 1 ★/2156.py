n = int(input())
a = [0] + [int(input()) for _ in range(n)]

ans = dict()
def f(n):
    if n in ans:
        return ans[n]
    
    if n == 1:
        return a[1]
    elif n == 2:
        return a[1] + a[2]
    elif n == 3:
        return max(a[1] + a[2], a[2] + a[3], a[1] + a[3])
    else:
        ans[n] = max(f(n - 1), f(n - 3) + a[n - 1] + a[n], f(n - 2) + a[n])
        return ans[n]

for i in range(3, n, 20):
    f(i) # to avoid recursion error (maximum recursion depth exceeded)

print(f(n))