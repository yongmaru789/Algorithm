from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for c in range(n):
        if visited[c] == False:
            bfs(n, computers, c, visited)
            answer += 1
    
    return answer

def bfs(n, computers, c, visited):
    visited[c] = True
    queue = deque()
    queue.append(c)
    
    while len(queue) > 0:
        c = queue.popleft()
        visited[c] = True
        
        for i in range(n):
            if visited[i] == False and computers[i][c] == 1 and i != c:
                queue.append(i)
        