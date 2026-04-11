import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = []

def backtracking(num):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    
    for i in range(num, N + 1):
        res.append(i)
        backtracking(i)
        res.pop()

backtracking(1)