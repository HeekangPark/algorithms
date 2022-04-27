import sys

nums = [0] * 10001

n = int(sys.stdin.readline())
for i in range(n):
    nums[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for j in range(nums[i]):
        print(i)