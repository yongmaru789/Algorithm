import sys
input = sys.stdin.readline
    
def mx(A, B):
    if B == 0:
        return A
    else:
        return mx(B, A % B)

N = int(input())
first_tree = int(input())

distance = []
for _ in range(N - 1):
    num = int(input())
    distance.append(num - first_tree)
    first_tree = num

d = distance[0]
for i in range(1, len(distance)):
    d = mx(d, distance[i])

result = 0
for j in distance:
    result += j // d - 1

print(result)