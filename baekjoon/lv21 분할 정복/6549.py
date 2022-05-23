import math
import sys
sys.setrecursionlimit(10 ** 6)

def _build(tree, arr, start, end, idx):
    if end - start == 1:
        tree[idx] = {
            "query": [start, end],
            "key": start,
            "value": arr[start]
        }
        return

    mid = (start + end) // 2
    
    _build(tree, arr, start, mid, idx * 2)
    _build(tree, arr, mid, end, idx * 2 + 1)
    
    left = tree[idx * 2]
    right = tree[idx * 2 + 1]

    tree[idx] = {
        "query": [start, end],
        "key": left["key"] if left["value"] <= right["value"] else right["key"],
        "value": left["value"] if left["value"] <= right["value"] else right["value"]
    }

def _getMin(tree, start, end, idx):
    if tree[idx]["query"][0] == start and tree[idx]["query"][1] == end:
        return tree[idx]

    mid = (tree[idx]["query"][0] + tree[idx]["query"][1]) // 2
    
    if end <= mid:
        return _getMin(tree, start, end, idx * 2)
    elif start >= mid:
        return _getMin(tree, start, end, idx * 2 + 1)
    else:
        left = _getMin(tree, start, mid, idx * 2)
        right = _getMin(tree, mid, end, idx * 2 + 1)
        return left if left["value"] <= right["value"] else right

def getMaxArea(tree, arr, start, end):
    if end - start == 1:
        return arr[start]

    minItem = _getMin(tree, start, end, 1)
    candidates = [minItem["value"] * (end - start)]
    if start < minItem["key"]:
        candidates.append(getMaxArea(tree, arr, start, minItem["key"]))
    if minItem["key"] + 1 < end:
        candidates.append(getMaxArea(tree, arr, minItem["key"] + 1, end))
    return max(candidates)

while True:
    line = list(map(int, input().split()))
    n, a = line[0], line[1:]
    if n == 0:
        break
    
    tree = [None] + [None] * (int(math.pow(2, int(math.log2(n)) + 2)) - 1)

    _build(tree, a, 0, n, 1)
    
    print(getMaxArea(tree, a, 0, n))