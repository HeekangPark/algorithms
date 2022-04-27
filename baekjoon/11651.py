import sys

n = int(sys.stdin.readline())
a = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
print("\n".join([f"{x[0]} {x[1]}" for x in a]))