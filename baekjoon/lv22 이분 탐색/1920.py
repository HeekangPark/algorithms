n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

def binary_search(target, start, end):
    mid = (start + end) // 2
    if end - start < 1:
        return False

    if a[mid] == target:
        return True
    elif a[mid] < target:
        return binary_search(target, mid + 1, end)
    else:
        return binary_search(target, start, mid)

for x in b:
    if binary_search(x, 0, n):
        print(1)
    else:
        print(0)

