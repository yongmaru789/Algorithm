def solution(n, words):
    used = set()
    used.add(words[0])
    
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in used:
            person = i % n + 1
            turn = i // n + 1
            return [person, turn]
        used.add(words[i])
        
    return [0, 0]