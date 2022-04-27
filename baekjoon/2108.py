import sys
from collections import Counter

n = int(sys.stdin.readline())
a = sorted([int(sys.stdin.readline()) for _ in range(n)])
print(round(sum(a) / n))
print(a[n//2])
x = Counter(a).most_common(2)
print(x[1][0] if len(x) == 2 and x[0][1] == x[1][1] else x[0][0])
print(a[-1] - a[0])