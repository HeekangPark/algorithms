ans = dict()
def f(n):
    if n in ans:
        return ans[n]
    
    if n == 1:
        ans[n] = 0
    else:
        candidates = [f(n - 1)] + ([f(n // 2)] if n % 2 == 0 else []) + ([f(n // 3)] if n % 3 == 0 else [])
        ans[n] = min(candidates) + 1
    return ans[n]

n = int(input())
for i in range(2, n, 18):
    f(i) # to avoid recursion error (maximum recursion depth exceeded)
print(f(n))
    