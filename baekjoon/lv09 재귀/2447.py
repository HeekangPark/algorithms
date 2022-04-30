n = int(input())
board = [["*" for _ in range(n)] for _ in range(n)]

def pop(x, y, length):
    for i in range(length):
        for j in range(length):
            board[x + i][y + j] = " "

def do(x, y, length):
    if length == 3:
        board[x + 1][y + 1] = " "
        return
    
    small_len = length // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                pop(x + i * small_len, y + j * small_len, small_len)
            else:
                do(x + i * small_len, y + j * small_len, small_len)

do(0, 0, n)
for i in range(n):
    print("".join(board[i]))