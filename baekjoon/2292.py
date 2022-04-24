def calc(n):
    return (3 + (12 * n - 3) ** 0.5) / 6

def isInt(x):
    if x == int(x):
        return True
    else:
        return False

n = int(input())

print(int(calc(n)) if isInt(calc(n)) else int(calc(n)) + 1)