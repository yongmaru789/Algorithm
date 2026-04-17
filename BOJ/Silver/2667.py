import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().strip())) for _ in range(N)]

cnt = 0
num = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def find_1(x, y):
    global cnt
    
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    
    if house[x][y] == 1:
        cnt += 1
        house[x][y] = 0
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            find_1(next_x, next_y)
        return True
    return False


cnt = 0
res = 0

for i in range(N):
    for j in range(N):
        if find_1(i, j) == True:
            num.append(cnt)
            res += 1
            cnt = 0

print(res)
num.sort()
for ans in num:
    print(ans)
