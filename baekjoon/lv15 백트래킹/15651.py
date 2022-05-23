def printAll(idx):
    if idx == m:
        print(' '.join(map(str, history)))
        return

    for i in range(1, n + 1):
        history[idx] = i
        printAll(idx + 1)

n, m = map(int, input().split())
history = [0] * m
printAll(0)
