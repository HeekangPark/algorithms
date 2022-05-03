ans = [0, 1, 1, 1, 2, 2]
for i in range(6, 101):
    ans.append(ans[i - 1] + ans[i - 5])

T = int(input())
for t in range(T):
    n = int(input())
    print(ans[n])