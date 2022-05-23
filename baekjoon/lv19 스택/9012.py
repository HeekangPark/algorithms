def check(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

n = int(input())
for _ in range(n):
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')