def getFactorNumInFactorial(n, factor):
    count = 0
    divisor = factor
    while divisor <= n:
        count += n // divisor
        divisor *= factor
    return count

n, m = map(int, input().split())
top2 = getFactorNumInFactorial(n, 2)
bottom2 = getFactorNumInFactorial(m, 2) + getFactorNumInFactorial(n - m, 2)
top5 = getFactorNumInFactorial(n, 5)
bottom5 = getFactorNumInFactorial(m, 5) + getFactorNumInFactorial(n - m, 5)
print(min((top2 - bottom2), (top5 - bottom5)))
