k, n = map(int, input().split())
origs = [int(input()) for _ in range(k)]

def count(length):
    return sum(orig // length for orig in origs)

def binary_search(count_target, len_start, len_end):
    if len_end - len_start < 1:
        return len_end - 1

    len_mid = (len_start + len_end) // 2
    len_mid_count = count(len_mid)

    if len_mid_count >= count_target:
        return binary_search(count_target, len_mid + 1, len_end)
    else:
        return binary_search(count_target, len_start, len_mid)

print(binary_search(n, 1, max(origs) + 1))