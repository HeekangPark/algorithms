n = int(input())
prices = [list(map(int, input().split())) for _ in range(n)]

ans = [[100000000] * 3 for _ in range(n)]
ans[0][0] = prices[0][0]
ans[0][1] = prices[0][1]
ans[0][2] = prices[0][2]
for i in range(1, n):
    ans[i][0] = min(ans[i - 1][1], ans[i - 1][2]) + prices[i][0]
    ans[i][1] = min(ans[i - 1][0], ans[i - 1][2]) + prices[i][1]
    ans[i][2] = min(ans[i - 1][0], ans[i - 1][1]) + prices[i][2]

print(min(ans[n - 1]))