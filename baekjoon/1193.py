'''
k = 1 [ 1] 1/1
k = 2 [ 5] 1/2 2/1 3/1 2/2 1/3
k = 3 [ 9] 1/4 2/3 3/2 4/1 5/1 4/2 3/3 2/4 1/5
k = 4 [13] 1/6 2/5 3/4 4/3 5/2 6/1 7/1 6/2 5/3 4/4 3/5 2/6 1/7


val: 1/6 2/5 3/4 4/3 5/2 6/1 7/1 6/2 5/3 4/4 3/5 2/6 1/7
gap:  12  11  10   9   8   7   6   5   4   3   2   1   0
'''

def calc_k(x):
    return (1 + (8 * x + 1)**0.5) / 4

def is_int(x):
    if x == int(x):
        return True
    else:
        return False

x = int(input())

k = calc_k(x)
if is_int(k):
    k = int(k)
else:
    k = int(k) + 1

top = 1
bottom = 2 * k - 1

sum_to_k = 2 * k * k - k
k_len = 4 * k - 3
gap = sum_to_k - x

if (k_len - 1) // 2 >= gap:

    print(f"{top + gap}/{bottom - gap}")
else:
    top = bottom - 1
    bottom = 1
    gap = gap - (k_len - 1) // 2 - 1
    print(f"{top - gap}/{bottom + gap}")
