n = int(input())
best_path = []
for i in range(1, n + 1):
    best_path = [max(best_path[j] if 0 <= j < len(best_path) else 0, best_path[j - 1] if 0 <= j - 1 < len(best_path) else 0) + val for j, val in enumerate(map(int, input().split()))]
print(max(best_path))