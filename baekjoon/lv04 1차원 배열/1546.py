n = int(input())
a = list(map(int, input().split()))
new = [x / max(a) * 100 for x in a]
print(sum(new) / len(new))