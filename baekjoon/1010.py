from math import comb

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    print(comb(m, n))