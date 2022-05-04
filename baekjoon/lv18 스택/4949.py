starts = ["(", "["]
ends = {")": "(", "]": "["}

def check(s):
    stack = []
    for i in s:
        if i in starts:
            stack.append(i)
        elif i in ends.keys():
            if len(stack) != 0 and stack[-1] == ends[i]:
                stack.pop()
                continue
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

while True:
    s = input()
    if s == ".":
        break
    
    if check(s):
        print('yes')
    else:
        print('no')