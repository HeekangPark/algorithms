N = int(input())
group_word_num = 0
for n in range(N):
    word = input()
    appeared = []
    cur = word[0]
    is_group_word = True
    for l in word[1:]:
        if l == cur:
            continue
        else:
            if l in appeared:
                is_group_word = False
                break
            else:
                appeared.append(cur)
                cur = l
    if is_group_word:
        group_word_num += 1

print(group_word_num)
