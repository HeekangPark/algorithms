n = int(input())
a = [int(input()) for _ in range(n)]

def check(a):
    result = []

    stack = [0]
    new = 1

    for i in range(n):
        if a[i] > stack[-1] and a[i] >= new:
            while new <= a[i]:
                stack.append(new)
                result.append("+")
                new += 1

        if stack[-1] == 0:
            return False, ""
            
        if a[i] == stack[-1]:
            stack.pop()
            result.append("-")
        else:
            return False, ""
    
    if stack[-1] == 0:
        return True, result
    else:
        return False, ""

result, result_str = check(a)
if result:
    print("\n".join(result_str))
else:
    print("NO")