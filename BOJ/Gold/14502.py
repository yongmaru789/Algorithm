from collections import deque

n, m = map(int, input().split())
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    queue = deque()
    # makeWall() 함수에서 벽 설치/제거를 반복해도 bfs()는 원본 상태에서 시작해야 하므로 원본 보호를 위해 복사한다.
    tmp = [row[:] for row in graph]

    # 바이러스(2) 위치를 모두 queue에 삽입한다.
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        # 상하좌우로 바이러스가 확산된다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 안에 있고, 빈 칸(0)인 경우에만 바이러스가 확산된다.
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                queue.append((nx, ny))

    # 남은 안전 영역(0)의 개수를 반환한다.
    cnt = 0    
    for i in range(n):
        cnt += tmp[i].count(0)
    return cnt

def makeWall(cnt):
    # 벽 3개가 완성되면 BFS로 바이러스 확산 시뮬레이션을 진행한 후, 안전 영역 개수를 반환한다.
    if cnt == 3:
        return bfs()
    
    answer = 0
    for i in range(n):
        for j in range(m):
            # 빈 칸(0)을 순서대로 탐색하며 벽(1)을 하나씩 놓고 재귀로 3개가 될 때까지 반복한다.
            if graph[i][j] == 0:
                graph[i][j] = 1
                answer = max(answer, makeWall(cnt+1))
                graph[i][j] = 0
    return answer

for i in range(n):
    graph.append(list(map(int, input().split())))
print(makeWall(0))
