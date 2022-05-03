ans = dict()
def f(length, startswith):
    if (length, startswith) in ans:
        return ans[(length, startswith)]
    
    if length == 1:
        ans[(length, startswith)] = 1
    else:
        ans[(length, startswith)] = ((f(length - 1, startswith - 1) if startswith - 1 >= 0 else 0) + (f(length - 1, startswith + 1) if startswith + 1 < 10 else 0)) % 1000000000

    return ans[(length, startswith)]

n = int(input())
print(sum([f(n, i) for i in range(1, 10)]) % 1000000000)