n = int(input())
x = n
count = 0
while True:
    count += 1
    x = (x % 10 + x // 10) % 10 + (x % 10) * 10
    if x == n:
        break

print(count)