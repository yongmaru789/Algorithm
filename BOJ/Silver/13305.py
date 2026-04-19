import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = 0
a = cost[0]

for i in range(N - 1):
    if cost[i] < a:
        a = cost[i]
    res += a * distance[i]

print(res)

