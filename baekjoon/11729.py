n = int(input())
print(2 ** n - 1)
def solve(from_pole, to_pole, other_pole, num):
    if num == 0:
        return
    solve(from_pole, other_pole, to_pole, num - 1)
    print(f"{from_pole} {to_pole}")
    solve(other_pole, to_pole, from_pole, num - 1)

solve(1, 3, 2, n)