import sys
input = sys.stdin.readline

a_num, b_num = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

print(a_num + b_num - 2 * len(a_set & b_set))