from collections import deque

def solution(n, wires):
    
    def bfs(n1, n2):
        result = 1
        visited = [False for _ in range(n+1)]
        queue = deque()
        queue.append(n1)
        visited[n1] = True
        # 연결된 송전탑 n2를 미리 방문 처리하여 탐색에서 제외
        visited[n2] = True
        
        while queue:
            node = queue.popleft()
            for g in graph[node]:
                if not visited[g]:
                    result += 1
                    visited[g] = True
                    queue.append(g)
        return result
    
    answer = n
    # graph : 인접리스트 방식으로 구현한 무방향 그래프
    graph = [[] for _ in range(n+1)]
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
        
    for n1, n2 in wires:
        # 각 간선을 하나씩 끊어보며(n1과 n2의 연결을 무시), 한쪽 네트워크의 노드 개수를 센다.
        result = bfs(n1, n2)
        diff = abs(result - (n-result))
        # 두 전력망의 송전탑 개수 차이 중 최솟값을 갱신한다.
        answer = min(answer, diff)
        
    return answer
    