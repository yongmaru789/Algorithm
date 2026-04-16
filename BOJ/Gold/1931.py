import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
new = sorted(meetings, key = lambda x : (x[1], x[0]))

cnt = 0
time = 0

for meeting in new:
    if meeting[0] >= time:
        time = meeting[1]
        cnt += 1

print(cnt)
