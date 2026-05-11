import sys
from collections import deque
input = sys.stdin.readline

# 위/아래/오른쪽/왼쪽/대각선
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,-1,1]

def bfs(x, y):
    q = deque()
    q.append([x,y])
    graph[y][x] = 0

    while q:
        curr_x, curr_y = q.popleft()
        for i in range(8):
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]

            if 0 <= next_x < w and 0 <= next_y < h:
                if graph[next_y][next_x] == 1:
                    graph[next_y][next_x] = 0
                    q.append([next_x, next_y])

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):   # y값
        for j in range(w):  # x값
            if graph[i][j] == 1:
                bfs(j,i)
                cnt += 1

    print(cnt)