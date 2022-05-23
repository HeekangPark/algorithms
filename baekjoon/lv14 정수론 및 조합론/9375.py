from functools import reduce

T = int(input())
for t in range(T):
    n = int(input())
    if n == 0:
        print(0)
    else:
        clothes = {}
        for _ in range(n):
            name, type = input().split()
            if type not in clothes:
                clothes[type] = []
            clothes[type].append(name)
        
        print(reduce(lambda x, y: x * y, [len(clothes[type]) + 1 for type in clothes]) - 1)