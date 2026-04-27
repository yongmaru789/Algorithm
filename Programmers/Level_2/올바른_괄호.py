def solution(s):
    count = 0
    
    for char in s:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
        if count < 0:
            return False
        
    ans = (count == 0)    
    return ans