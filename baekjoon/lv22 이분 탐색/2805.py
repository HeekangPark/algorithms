# Python3으로 제출하면 시간초과가 나옴
# PyPy3으로 제출할 것

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

def calc(height):
    total = 0
    for i in range(n):
        if a[i] >= height:
            total += a[i] - height
    return total

height_start = 0
height_end = max(a) + 1

while height_end - height_start >= 1:
    if height_end - height_start < 1:
        break

    height_mid = (height_start + height_end) // 2
    height_mid_amount = calc(height_mid)

    if height_mid_amount >= m:
        height_start = height_mid + 1
    else:
        height_end = height_mid

    
print(height_end - 1)