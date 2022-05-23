n = int(input())
a = sorted(map(int, input().split()))
if len(a) == 1:
    print(a[0] * a[0])
else:
    print(a[0] * a[-1])
