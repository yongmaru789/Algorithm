import heapq

def solution(operations):
    
    max_heap = []
    min_heap = []
    visited = [False] * len(operations)
    
    for idx, op in enumerate(operations):
        command, n = op.split()
        if command == "I":
            heapq.heappush(max_heap, (-int(n), idx))
            heapq.heappush(min_heap, (int(n), idx))
            visited[idx] = True
            
        elif command == "D" and int(n) == 1:
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                _, key = heapq.heappop(max_heap)
                visited[key] = False
        elif command == "D" and int(n) == -1:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                _, key = heapq.heappop(min_heap)
                visited[key] = False
                
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if not max_heap or not min_heap:
        return [0, 0]
    else:
        return [-max_heap[0][0], min_heap[0][0]]
