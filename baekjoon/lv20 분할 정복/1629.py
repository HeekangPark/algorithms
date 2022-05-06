a, b, c = map(int, input().split())

ans = {}
def mul(b):
    if b in ans:
        return ans[b]
    
    if b == 0:
        return 1
    elif b == 1:
        return a % c

    if b % 2 == 0:
        ans[b] = mul(b // 2) * mul(b // 2)
    else:
        ans[b] = mul(b // 2) * mul(b // 2) * a
    ans[b] %= c
    return ans[b]

print(mul(b))
