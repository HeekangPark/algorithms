from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    imps = list(map(int, input().split()))
    sorted_imps = sorted(imps, reverse=True)
    sorted_imps_idx = 0

    q = deque(range(n))
    while len(q) > 0:
        idx = q.popleft()
        if sorted_imps[sorted_imps_idx] == imps[idx]:
            if idx == m:
                print(sorted_imps_idx + 1)
                break
            else:
                sorted_imps_idx += 1
        else:
            q.append(idx)
        
