n = int(input())
words = sorted(set([input() for _ in range(n)]), key=lambda x: (len(x), x))
print("\n".join(words))
