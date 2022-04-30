# Python3으로 제출하면 시간초과가 나옴
# PyPy3으로 제출할 것

import sys

board = [[0] * 9 for _ in range(9)]
avail = {}
for i in range(9):
    line = list(map(int, input().split()))
    for j in range(9):
        board[i][j] = line[j]
        if line[j] == 0:
            avail[(i, j)] = list(range(1, 10))

for x, y in avail.keys():
    # horizontal
    for i in range(9):
        num = board[x][i]
        if num in avail[(x, y)]:
            avail[(x, y)].remove(num)

    # vertical
    for i in range(9):
        num = board[i][y]
        if num in avail[(x, y)]:
            avail[(x, y)].remove(num)

    # square
    for i in range(3):
        for j in range(3):
            num = board[x // 3 * 3 + i][y // 3 * 3 + j]
            if num in avail[(x, y)]:
                avail[(x, y)].remove(num)

avail_list = list(avail.items())

def check(x, y, num):
    # horizontal
    for i in range(9):
        if board[x][i] == num:
            return False
    
    # vertical
    for i in range(9):
        if board[i][y] == num:
            return False

    # square
    for i in range(3):
        for j in range(3):
            if board[x // 3 * 3 + i][y // 3 * 3 + j] == num:
                return False

    return True

def search(idx):
    if idx == len(avail_list):
        printBoard()
        sys.exit(0)


    x, y = avail_list[idx][0]
    nums = avail_list[idx][1]
    for num in nums:
        if check(x, y, num):
            board[x][y] = num
            search(idx + 1)
            board[x][y] = 0
                
def printBoard():
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()

search(0)