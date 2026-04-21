import sys
input = sys.stdin.readline

def dfs(idx, sour, bitter, cnt):
    global minimum

    if idx == N:
        if cnt > 0:
            minimum = min(minimum, abs(sour - bitter))     
        return
    
    dfs(idx + 1, sour * tastes[idx][0], bitter + tastes[idx][1], cnt + 1)
    dfs(idx + 1, sour, bitter, cnt)
        


N = int(input())
tastes = [list(map(int, input().split())) for _ in range(N)]

minimum = float('inf')

dfs(0, 1, 0, 0)
print(minimum)