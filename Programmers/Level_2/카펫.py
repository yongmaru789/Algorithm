import math

def solution(brown, yellow):
    answer = []    
    w, h = 0, 0
    
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            w, h = yellow // i, i
            if brown == 2 * (w + h) + 4:
                break
    
    answer.append(w + 2)
    answer.append(h + 2)
    return answer