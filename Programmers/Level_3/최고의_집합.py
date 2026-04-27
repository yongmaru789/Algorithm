def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    num = s // n
    left = s % n
    for idx in range(n):
        answer.append(num)
    if left != 0:
        for i in range(n):
            answer[i] += 1
            left -= 1
            if left == 0:
                break
                
    answer.sort()
    return answer