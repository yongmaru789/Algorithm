import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = []

def backtracking(num):
    if len(res) == M:
        print(' '.join(map(str, res)))
    
    for i in range(num, N + 1):
        if i not in res:
            res.append(i)
            backtracking(i + 1)
            res.pop()

backtracking(1)