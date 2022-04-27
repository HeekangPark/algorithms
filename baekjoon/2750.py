n = int(input())
a = [int(input()) for _ in range(n)]
print("\n".join(map(str, sorted(a))))