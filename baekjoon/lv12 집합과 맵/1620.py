import sys
input = sys.stdin.readline

n, m = map(int, input().split())

book = [input().strip() for _ in range(n)]
questions = [input().strip() for _ in range(m)]

book = dict({name: str(id) for id, name in enumerate(book, 1)}, **{str(id): name for id, name in enumerate(book, 1)})

print("\n".join([book[question] for question in questions]))