n = int(input())
operands = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_val = -1000000001
min_val = 1000000001

def search(idx, val):
    global min_val, max_val
    
    if idx == n:
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val
        return
    
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1

            if i == 0:
                search(idx + 1, val + operands[idx])
            elif i == 1:
                search(idx + 1, val - operands[idx])
            elif i == 2:
                search(idx + 1, val * operands[idx])
            elif i == 3:
                if val < 0:
                    search(idx + 1, -(abs(val) // operands[idx]))
                else:
                    search(idx + 1, val // operands[idx])
            
            operators[i] += 1

search(1, operands[0])
print(max_val)
print(min_val)