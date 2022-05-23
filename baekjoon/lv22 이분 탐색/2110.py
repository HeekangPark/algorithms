import sys
from itertools import accumulate

input = sys.stdin.readline

n, c = map(int, input().split())
xs = sorted([int(input()) for _ in range(n)])

ds = [xs[i + 1] - xs[i] for i in range(n - 1)]

cumsum = [0] + list(accumulate(ds, lambda x, y: x + y))
def getRangeSum(start, end):
    if end - start < 1:
        return 0
    return cumsum[end] - cumsum[start]

def count(min_d_idx):
    min_d = ds[min_d_idx]
    count = 0

    range_start_idx = min_d_idx - 1
    range_end_idx = min_d_idx

    while range_start_idx >= 0:
        if getRangeSum(range_start_idx, range_end_idx) >= min_d:
            range_end_idx = range_start_idx
            count += 1

        range_start_idx -= 1

    range_start_idx = min_d_idx + 1
    range_end_idx = min_d_idx + 2
    while range_end_idx <= len(ds):
        if getRangeSum(range_start_idx, range_end_idx) >= min_d:
            range_start_idx = range_end_idx
            count += 1

        range_end_idx += 1
    
    return count

sorted_ds = sorted([{
    "idx": i,
    "value": d
} for i, d in enumerate(ds)], key=lambda x: x["value"])

search_start_idx = 0
search_end_idx = len(sorted_ds)

while search_end_idx - search_start_idx >= 1:
    search_mid_idx = (search_start_idx + search_end_idx) // 2
    
    mid_idx_count = count(sorted_ds[search_mid_idx]["idx"])
    if mid_idx_count >= c:
        search_start_idx = search_mid_idx + 1
    else:
        search_end_idx = search_mid_idx

print(sorted_ds[search_end_idx]["value"])
