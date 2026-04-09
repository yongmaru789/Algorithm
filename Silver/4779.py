import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def Cantor(N):
    if N == 1:
        return "-"
    else:
        left_right = Cantor(N // 3)
        center = " " * (N // 3)
        return left_right + center + left_right

for line in sys.stdin:
    if not line.strip():
        continue
    
    N = int(line)

    res = Cantor(3 ** N)
    print(res)

