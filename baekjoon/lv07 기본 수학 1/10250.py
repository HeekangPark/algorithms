T = int(input())
for t in range(T):
    h, w, n = map(int, input().split())
    print(f"{(n - 1)%h + 1}{(n - 1) // h + 1:02d}")
'''

h, w = 6, 12
for n in range(1, h * w + 1):
    print(f"{n} : {(n - 1)%h + 1}{(n - 1) // h + 1:02d}")
'''