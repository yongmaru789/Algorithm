from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [-1] * (n+1)
    
    # 연결된 노드에 대하여 정보 추가
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    queue = deque([1])
    distance[1] = 0
    
    while queue:
        curr = queue.popleft()
        
        # 현재 노드에서 갈 수 있는 모든 경로를 확인
        for i in graph[curr]:
            # 아직 방문하지 않은 노드면 queue에 추가하고, 현재 거리에 +1 해서 최단거리를 갱신한다.
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[curr] + 1
               
    # 가장 멀리 떨어진 노드의 갯수를 구한다.
    max_dist = max(distance)
    for d in distance:
        if d == max_dist:
            answer += 1
    return answer