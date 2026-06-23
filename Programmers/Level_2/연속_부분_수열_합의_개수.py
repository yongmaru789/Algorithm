def solution(elements):
    answer = set()
    length = len(elements)
    new_elements = elements * 2
    
    for i in range(length):
        for j in range(i+1, i+length+1):
            answer.add(sum(new_elements[i:j]))
    
    return len(answer)