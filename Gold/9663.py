import sys
input = sys.stdin.readline

N = int(input())
row = [0] * N

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False    
    return True

def n_queen(x):
    if x == N:
        return 1
    
    cnt = 0    
    for i in range(N):
        row[x] = i
        if is_promising(x):
            cnt += n_queen(x + 1)
    return cnt

print(n_queen(0))