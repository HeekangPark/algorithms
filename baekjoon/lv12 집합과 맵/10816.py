import sys
input = sys.stdin.readline

n = int(input())
haves = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

count = dict()
for have in haves:
    if have in count:
        count[have] += 1
    else:
        count[have] = 1

print(" ".join(map(str, [count[num] if num in count.keys() else 0 for num in nums])))