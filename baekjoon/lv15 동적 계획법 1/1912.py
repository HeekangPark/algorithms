n = int(input())
a = list(map(int, input().split()))

cumsum = [0]
for i in range(n):
    cumsum.append(cumsum[-1] + a[i])

d = []
minVal = cumsum[0]
for i in range(1, n + 1):
    d.append(cumsum[i] - minVal)
    if minVal > cumsum[i]:
        minVal = cumsum[i]

print(max(d))