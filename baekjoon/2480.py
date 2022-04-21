from collections import Counter

nums = list(map(int, input().split()))
count = sorted(dict(Counter(nums)).items(), key=lambda x: x[1], reverse=True)

if count[0][1] == 3:
    print(10000 + count[0][0] * 1000)
elif count[0][1] == 2:
    print(1000 + count[0][0] * 100)
else:
    print(max(nums) * 100)
