n = int(input())
info = [input().split() for _ in range(n)]
info = [[int(x[0]), x[1]] for x in info]
info = sorted(info, key=lambda x: x[0])
print("\n".join([f"{x[0]} {x[1]}" for x in info]))