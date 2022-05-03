ans = [0, 1, 2]
n = int(input())
for i in range(3, n + 1):
    ans.append((ans[i - 1] + ans[i - 2]) % 15746)

print(ans[n])