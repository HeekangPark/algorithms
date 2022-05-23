import sys
input = sys.stdin.readline

n, w, h = map(int, input().split())
lens = [int(input()) for _ in range(n)]
max_len_sqr = w * w + h * h

print(*["DA" if l * l <= max_len_sqr else "NE" for l in lens], sep='\n')