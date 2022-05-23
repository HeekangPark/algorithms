n, k = map(int, input().split())
p =  1000000007

k = min(k, n - k)

fact = 1
for i in range(n + 1):
    if i == 0:
        fact *= 1
    else:
        fact = (fact * i) % p
    
    if i == k:
        a = fact
    
    if i == n - k:
        b = fact
    
    if i == n:
        c = fact

a = (a * b) % p

ans = {}
def pow(x):
    if x in ans:
        return ans[x]
    if x == 0:
        return 1
    elif x == 1:
        return a
    else:
        if x % 2 == 0:
            ans[x] = (pow(x // 2) * pow(x // 2)) % p
        else:
            ans[x] = (pow(x // 2) * pow(x // 2) * a) % p

        return ans[x]

print((pow(p - 2) * c) % p)


