def solution(citations):
    citations.sort()
    n = len(citations)
    answer = 0
    for i, c in enumerate(citations):
        if c >= n - i:
            answer = n - i
            break
        
    return answer