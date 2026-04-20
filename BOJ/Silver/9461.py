import sys
input = sys.stdin.readline

arr = [0, 1, 1, 1] + [0 for x in range(97)]

def padovan(n):
    if arr[n]:
        return arr[n]
    else:
        arr[n] = padovan(n-2) + padovan(n-3)
        return arr[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(padovan(N))

