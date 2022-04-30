n = int(input())

count = 0
divisor = 5
while divisor <= n:
    count += n // divisor
    divisor *= 5

print(count)