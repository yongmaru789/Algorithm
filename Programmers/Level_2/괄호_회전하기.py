def check(words):
    stack = []
    for w in words:
        if w == '(' or w == '[' or w == '{':
            stack.append(w)
        else:
            if len(stack) == 0:
                return False
            if w == ')' and stack.pop() != '(':
                return False
            if w == ']' and stack.pop() != '[':
                return False
            if w == '}' and stack.pop() != '{':
                return False
    return True

def solution(s):
    answer = 0
    if len(s) % 2 != 0:
        return answer
    
    s = list(s)
    if check(s):
        answer += 1
    
    for _ in range(len(s) - 1):
        x = s.pop(0)
        s.append(x)        
        if check(s):
            answer += 1
            
    return answer