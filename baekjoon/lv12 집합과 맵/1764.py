import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hear = set(input().strip() for _ in range(n))
see = set(input().strip() for _ in range(m))

both = hear & see
print(len(both))
print(*sorted(list(both)), sep='\n')
