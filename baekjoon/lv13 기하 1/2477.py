import sys
input = sys.stdin.readline

correct_orders = [
    [1, 4, 2, 3],
    [2, 3, 1, 4],
    [3, 1, 4, 2],
    [4, 2, 3, 1],
]

k = int(input())
w = 0
h = 0
correct_order = None
order_idx = 0
sides = []
mw = None
mh = None
for i in range(6):
    dir, length = map(int, input().split())

    if correct_order is None:
        correct_order = correct_orders[dir - 1]
    else:
        if mw is None and mh is None and correct_order[order_idx] != dir:
            mw = sides[-1][1]
            mh = length
    
    sides.append((dir, length))

    if dir in [1, 2]:
        w = max(w, length)
    else:
        h = max(h, length)
    
    order_idx = (order_idx + 1) % 4

if mw is None and mh is None:
    mw = sides[0][1]
    mh = sides[-1][1]

print((w * h - mw * mh) * k)