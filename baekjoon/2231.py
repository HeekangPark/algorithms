n = int(input())

found = False
for i in range(1, n):
    if i + sum(list(map(int, str(i)))) == n:
        print(i)
        found = True
        break

if found == False:
    print(0)