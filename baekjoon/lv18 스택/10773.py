import sys

k = int(sys.stdin.readline())
l = []
for _ in range(k):
    x = int(sys.stdin.readline())
    if x != 0:
        l.append(x)
    else:
        l.pop()

print(sum(l))