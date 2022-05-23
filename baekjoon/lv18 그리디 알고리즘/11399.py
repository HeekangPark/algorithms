n = int(input())
t = sorted(map(int, input().split()))
total = 0
for i in range(n):
    total += t[i] * (n - i)

print(total)