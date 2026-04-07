import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, M = map(int, input().split())

    res = 1
    for i in range(N):
        res *= M
        M -= 1

    div = 1
    for i in range(2, N+1):
        div *= i

    print(res // div)