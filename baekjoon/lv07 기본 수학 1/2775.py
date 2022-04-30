T = int(input())

for t in range(T):
    K, N = [int(input()) for _ in range(2)]
    
    people_num = [i + 1 for i in range(N)]

    for k in range(1, K + 1):
        people_num = [sum(people_num[:i + 1]) for i in range(N)]

    print(people_num[-1])