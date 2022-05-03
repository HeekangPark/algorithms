n, k = map(int, input().split())
a = list(map(int, input().split()))

psum = sum(a[:k])
max_val = psum
for i in range(k, n):
    psum = psum - a[i - k] + a[i]
    if psum > max_val:
        max_val = psum

print(max_val)
