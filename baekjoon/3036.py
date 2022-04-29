from fractions import Fraction

n = int(input())
rs = list(map(int, input().split()))
answer = [Fraction(f"{rs[0]}/{r}") for r in rs[1:]]
print("\n".join([f"{r.numerator}/{r.denominator}" for r in answer]))