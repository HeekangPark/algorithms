n = int(input())

a = n // 5
k = -1
while a >= 0:
    if (n - a * 5) % 3 == 0:
        k = a + (n - a * 5) // 3
        break
    a -= 1
print(k)
