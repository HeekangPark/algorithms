import sys

word = sys.stdin.readline().strip()

x = set()
for i in range(len(word)):
    for j in range(i + 1, len(word) + 1):
        x.add(word[i:j])
print(len(x))

