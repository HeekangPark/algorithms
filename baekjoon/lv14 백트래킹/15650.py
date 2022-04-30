def printAll(idx):
    if idx == m + 1:
        print(' '.join(map(str, history[1:])))
        return

    for i in range(history[idx - 1] + 1, n + 1):
        history[idx] = i
        printAll(idx + 1)

n, m = map(int, input().split())
history = [0] * (m + 1)
printAll(1)
