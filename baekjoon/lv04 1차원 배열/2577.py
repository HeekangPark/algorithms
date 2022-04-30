a, b, c = [int(input()) for x in range(3)]
x = str(a * b * c)
print('\n'.join([str(sum([1 for j in x if int(j) == i])) for i in range(10)]))