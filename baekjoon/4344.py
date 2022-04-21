c = int(input())

for i in range(c):
    a = list(map(int, input().split()))
    n = a[0]
    a = a[1:]
    mean = sum(a) / len(a)
    print(f"{sum([1 for x in a if x > mean]) / n * 100:.3f}%")