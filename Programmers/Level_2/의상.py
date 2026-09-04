from collections import Counter

def solution(clothes):
    counts = Counter(type for name, type in clothes)
    
    answer = 1    
    for cnt in counts.values():
        answer *= (cnt + 1)
    return answer - 1
    