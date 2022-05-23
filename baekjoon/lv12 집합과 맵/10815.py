n = int(input())
a = sorted(list(map(int, input().split())))

m = int(input())
b = list(map(int, input().split()))

def search(target, start, end):
    if end - start < 1:
        return False
    
    mid = (start + end) // 2
    
    if a[mid] == target:
        return True
    elif a[mid] < target:
        return search(target, mid + 1, end)
    else:
        return search(target, start, mid)
    
print(" ".join(map(str, [1 if search(x, 0, n) else 0 for x in b])))