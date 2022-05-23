# Python3으로 제출하면 시간초과가 나옴
# PyPy3으로 제출할 것

import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

def binary_search_find_start(target, start, end):
    if end - start < 1:
        return start

    mid = (start + end) // 2
    if a[mid] < target:
        return binary_search_find_start(target, mid + 1, end)
    else:
        return binary_search_find_start(target, start, mid)

def binary_search_find_end(target, start, end):
    if end - start < 1:
        return end

    mid = (start + end) // 2
    if a[mid] > target:
        return binary_search_find_end(target, start, mid)
    else:
        return binary_search_find_end(target, mid + 1, end)

print(" ".join([str(binary_search_find_end(x, 0, n) - binary_search_find_start(x, 0, n)) for x in b]))

# 걍 dict로 짜면 python3에서도 돌릴 수 있다.

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

count = {}
for x in a:
    if x not in count:
        count[x] = 1
    else:
        count[x] += 1

for x in b:
    if x in count:
        print(count[x])
    else:
        print(0)