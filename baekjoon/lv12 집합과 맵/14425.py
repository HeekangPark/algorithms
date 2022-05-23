import sys
input = sys.stdin.readline

n, m = map(int, input().split())
testing_words = [input() for _ in range(n)]
tested_words = [input() for _ in range(m)]

count = 0
for tested_word in tested_words:
    if tested_word in testing_words:
        count += 1

print(count)
