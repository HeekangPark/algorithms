# Python3으로 제출하면 시간초과가 나옴
# PyPy3으로 제출할 것

def canPlace(x, y):
    for i in range(x):
        if ys[i] == y:  # check vertical
            return False
        if x - i == abs(y - ys[i]):  # check diagonal
            return False
        
    return True

def search(idx):
    global count
    if idx == n:
        count += 1
        return
    
    for i in range(n):
        if canPlace(idx, i):
            ys[idx] = i
            search(idx + 1)

import sys
n = int(sys.stdin.readline())

count = 0
ys = [-1] * n

if n == 1:
    print(1)
else:
    for i in range(n // 2): # 절반만 탐색
        ys[0] = i
        search(1)
    count *= 2

    if n % 2 == 1:
        ys[0] = n // 2
        search(1)

    print(count)
