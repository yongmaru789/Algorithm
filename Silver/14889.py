import sys
input = sys.stdin.readline

N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]
team = [False for _ in range(N)]
res = float('inf')

def dfs(depth, idx):
    global res
    
    if depth == N//2:
        first = 0
        second = 0
        for i in range(N):
            for j in range(i+1, N):
                if team[i] and team[j]:
                    first += stats[i][j] + stats[j][i]
                elif not team[i] and not team[j]:
                    second += stats[i][j] + stats[j][i]
        res = min(res, abs(first - second))
        return

    for i in range(idx, N):
        if not team[i]:
            team[i] = True
            dfs(depth + 1, i + 1)
            team[i] = False

dfs(0, 0)
print(res)


