import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))

INF = float('inf')
dist = [INF] * (N+1)

def bellman_ford(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            now, next, time = edges[j]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 빠른 경우
            if dist[now] != INF and dist[next] > dist[now] + time:
                dist[next] = dist[now] + time

                if i == N-1:
                    return True

    return False

if bellman_ford(1):
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])

