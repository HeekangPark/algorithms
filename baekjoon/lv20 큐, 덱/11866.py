from collections import deque

n, k = map(int, input().split())

result = []
q = deque(range(1, n+1))
while len(q) > 0:
    for i in range(k - 1):
        q.append(q.popleft())
    result.append(q.popleft())

print(f"<{', '.join(map(str, result))}>")