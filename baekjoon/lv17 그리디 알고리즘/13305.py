n = int(input())
ls = list(map(int, input().split()))
ps = list(map(int, input().split()))

cur_p = 1000000001
result = 0
for i, p in enumerate(ps[:-1]):
    if cur_p > p:
        cur_p = p
    result += ls[i] * cur_p

print(result)
