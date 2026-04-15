import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
num = list(map(int, input().split()))

def oper(num):
    global arr, N, M

    if num == 1:
        arr = arr[::-1]

    elif num == 2:
        arr = [row[::-1] for row in arr]
        
    elif num == 3:
        tmp = [[0 for _ in range(N)] for _ in range(M)]
        for i in range(N):
            for j in range(M):
                tmp[j][N - 1 - i] = arr[i][j]
        arr = tmp
        N, M = M, N

    elif num == 4:
        tmp = [[0 for _ in range(N)] for _ in range(M)]
        for i in range(N):
            for j in range(M):
                tmp[M - 1 - j][i] = arr[i][j]
        arr = tmp
        N, M = M, N

    elif num == 5:
        tmp = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N//2):
            for j in range(M//2):
                tmp[i][j + M//2] = arr[i][j]
                tmp[i + N//2][j + M//2] = arr[i][j + M//2]
                tmp[i + N//2][j] = arr[i + N//2][j + M//2]
                tmp[i][j] = arr[i + N//2][j]
        arr = tmp
    
    elif num == 6:
        tmp = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N//2):
            for j in range(M//2):
                tmp[i + N//2][j] = arr[i][j]
                tmp[i][j] = arr[i][j + M//2]
                tmp[i][j + M//2] = arr[i + N//2][j + M//2]
                tmp[i + N//2][j + M//2] = arr[i + N//2][j]
        arr = tmp

for n in num:
    oper(n)
for row in arr:
    print(*row)

