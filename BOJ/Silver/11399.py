import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
times.sort()

res = 0
wait = 0

for t in times:
    wait += t
    res += wait

print(res)