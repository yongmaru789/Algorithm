from collections import Counter 

def solution(want, number, discount):
    answer = 0
    count = {}
    for i in range(len(want)):
        count[want[i]] = number[i]
    
    for i in range(len(discount) - 9):
        if count == Counter(discount[i:i+10]):
            answer += 1
            
    return answer