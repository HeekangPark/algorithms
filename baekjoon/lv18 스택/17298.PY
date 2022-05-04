n = int(input())
a = list(map(int, input().split()))

stack = [(a[0], 0)]
result = [0] * n
for i in range(1, n):
    while stack and stack[-1][0] < a[i]:
        item = stack.pop()
        result[item[1]] = a[i]
    
    stack.append((a[i], i))

while stack:
    item = stack.pop()
    result[item[1]] = -1

print(" ".join(map(str, result)))
