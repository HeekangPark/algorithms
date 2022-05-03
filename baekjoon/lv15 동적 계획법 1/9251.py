w1, w2 = [input() for _ in range(2)]

w2_dict = {}
for i, c in enumerate(w2):
    if c not in w2_dict:
        w2_dict[c] = []
    w2_dict[c].append(i + 1)
w2_dict[" "] = [0]

w1 = [" "] + [c for c in w1 if c in w2_dict]

ans = dict()
def f(new_idx, weight):
    if (new_idx, weight) in ans:
        return ans[(new_idx, weight)]
    
    if new_idx == 1:
        return 1

    longest_len = 0

    # 내 이전 글자들 중, 나보다 weight가 작은 글자 뒤에 붙일 수 있다.

    for existing_idx in range(1, new_idx):
        existing_c = w1[existing_idx]
        weights_of_existing_c = w2_dict[existing_c]
        for weight_of_existing_c in weights_of_existing_c:
            if weight > weight_of_existing_c:
                new_len = f(existing_idx, weight_of_existing_c) + 1
                if new_len > longest_len:
                    longest_len = new_len
    
    ans[(new_idx, weight)] = longest_len
    return ans[(new_idx, weight)]

lcs = 0
for new_idx in range(1, len(w1)):
    new_c = w1[new_idx]
    weights_of_new_c = w2_dict[new_c]
    for weight_of_new_c in weights_of_new_c:
        new_len = f(new_idx, weight_of_new_c)
        if new_len > lcs:
            lcs = new_len

print(lcs)