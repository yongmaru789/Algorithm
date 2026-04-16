import sys
input = sys.stdin.readline

def draw_stars(n):
    if n == 1:
        return ['*']

    stars = draw_stars(n // 3)
    tmp = []

    for s in stars:
        tmp.append(s * 3)
    for s in stars:
        tmp.append(s + ' '*(n // 3) + s)
    for s in stars:
        tmp.append(s * 3)

    return tmp

N = int(input())
print('\n'.join(draw_stars(N)))
