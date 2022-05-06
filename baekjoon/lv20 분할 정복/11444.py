def mul(a, b, p=1000000007):
    ax = len(a)
    ay = len(a[0])
    bx = len(b)
    by = len(b[0])

    if ay != bx:
        raise Exception('invalid matrix')

    c = [[0] * by for _ in range(ax)]
    for i in range(ax):
        for j in range(by):
            val = sum([a[i][k] * b[k][j] for k in range(ay)])
            while val < 0:
                val += p
            c[i][j] = val % p

    return c

def pow(a, n):
    ax = len(a)
    ay = len(a[0])
    
    if n == 0:
        return [[1 if i == j else 0 for j in range(ay)] for i in range(ax)]

    if n == 1:
        return a
    
    if n % 2 == 0:
        return pow(mul(a, a), n // 2)
    else:
        return mul(a, pow(mul(a, a), (n - 1) // 2))

n = int(input())
f = [
    [0, 1],
    [0, 0]
]
a = [
    [0, 1],
    [1, 1]
]
print(mul(f, pow(a, n - 1))[0][1])