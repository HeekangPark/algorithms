a, b = map(int, input().split())
c = int(input())

total = (a * 60 + b + c) % (24 * 60)
print(total // 60, total % 60)