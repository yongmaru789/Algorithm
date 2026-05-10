from collections import Counter

def solution(k, tangerine):
    answer = 0
    result = 0
    
    tmp = Counter(tangerine)
    tmp = tmp.most_common()
    
    for i in tmp:
        result += i[1]
        answer += 1
        if (result >= k):
            return answer