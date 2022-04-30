n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

def calcTeamStat(members):
    stat = 0
    for i in range(len(members)):
        for j in range(len(members)):
            stat += s[members[i]][members[j]]
    
    return stat

team1 = [-1] * (n // 2)
min_stat_diff = 100000000

def search(idx):
    global min_stat_diff
    
    if idx == n // 2:
        team1_stat = calcTeamStat(team1)
        
        team2 = [i for i in range(n) if i not in team1]
        team2_stat = calcTeamStat(team2)

        if abs(team1_stat - team2_stat) < min_stat_diff:
            min_stat_diff = abs(team1_stat - team2_stat)
        
        return

    for i in range(0 if idx == 0 else team1[idx - 1] + 1, n):
        team1[idx] = i
        search(idx + 1)

search(0)
print(min_stat_diff)