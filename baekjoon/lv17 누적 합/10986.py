n, m = map(int, input().split())
a = list(map(int, input().split()))

remains = dict()
cumsum = 0
remains[cumsum] = 1
for i in range(n):
    cumsum = (cumsum + a[i]) % m
    if cumsum not in remains:
        remains[cumsum] = 0
    remains[cumsum] += 1

#print(remains)
print(sum([(r_num * (r_num - 1) // 2) for r_num in remains.values()]))