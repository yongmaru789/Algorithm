import sys
input = sys.stdin.readline

N = int(input())
price = [list(map(int, input().split())) for _ in range(N)]
res = [[0] * 3 for _ in range(N)]

res[0][0], res[0][1], res[0][2] = price[0][0], price[0][1], price[0][2]

for i in range(1, N):
    res[i][0] = min(res[i - 1][1] + price[i][0], res[i - 1][2] + price[i][0])
    res[i][1] = min(res[i - 1][0] + price[i][1], res[i - 1][2] + price[i][1])
    res[i][2] = min(res[i - 1][0] + price[i][2], res[i - 1][1] + price[i][2])

print(min(res[N-1][0], res[N-1][1], res[N-1][2]))