a = [int(input()) for i in range(9)]
print(max(a))
print([i for i in range(9) if a[i] == max(a)][0] + 1)