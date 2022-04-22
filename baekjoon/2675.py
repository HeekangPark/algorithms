T = int(input())
for t in range(T):
    inputs = input().split()
    R = int(inputs[0])
    S = inputs[1]
    print(''.join([s * R for s in S]))