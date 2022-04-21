n, x = map(int, input().split())
a = list(map(int, input().split()))
print(' '.join([str(item) for item in a if item < x]))