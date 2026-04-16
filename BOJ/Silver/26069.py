import sys
input = sys.stdin.readline

N = int(input())
dance = {'ChongChong'}

for i in range(N):
    A, B = input().strip().split()

    if A in dance:
        dance.add(B)
    if B in dance:
        dance.add(A)

print(len(dance))