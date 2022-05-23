from math import comb

n, r = map(int, input().split())
print(comb(n, r) % 10007)