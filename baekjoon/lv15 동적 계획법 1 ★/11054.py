n = int(input())
a = list(map(int, input().split()))

def getD(arr):
    arr = [0] + arr

    d = [0]
    for i in range(1, n + 1):
        d.append(max([d[j] for j in range(i) if arr[j] < arr[i]]) + 1)
    
    return d[1:]

d1 = getD(a)
d2 = getD(a[::-1])[::-1]
d = [d1[i] + d2[i] - 1 for i in range(n)]
print(max(d))

