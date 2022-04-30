def isHan(x):
    x = str(x)
    if len(x) <= 2:
        return True
    gap = int(x[1]) - int(x[0])
    for i in range(2, len(x)):
        if int(x[i]) - int(x[i - 1]) != gap:
            return False
    return True

n = int(input())
print(sum([1 for x in range(1, n + 1) if isHan(x)]))
