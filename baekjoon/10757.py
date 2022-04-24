a, b = input().split()

length = max(len(a), len(b)) + 1

a = list(map(int, a.zfill(length)))[::-1]
b = list(map(int, b.zfill(length)))[::-1]
result = [0] * length
carry =  [0] * (length + 1)
for i in range(length):
    calc = a[i] + b[i] + carry[i]
    result[i] = calc % 10
    carry[i + 1] = calc // 10

print(int(''.join([str(x) for x in result])[::-1]))