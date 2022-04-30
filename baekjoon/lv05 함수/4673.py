to = 10000
calc = lambda n: n + sum([int(x) for x in str(n)])
board = list(range(to + 1))
for i in range(1, to + 1):
    if calc(i) <= to:
        board[calc(i)] = -1
print('\n'.join([str(x) for x in board if x != -1 and x != 0]))