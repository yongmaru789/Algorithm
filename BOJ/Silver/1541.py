import sys
input = sys.stdin.readline

num = input().split('-')

sub = []
for i in num:
    tmp = list(map(int, i.split('+')))
    sub.append(sum(tmp))

res = sub[0]
for i in sub[1:]:
    res -= i

print(res)