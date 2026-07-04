import sys
input = sys.stdin.readline

check = [0] * 1000001
check[0] = 1
check[1] = 1
is_prime = []

for i in range(2, 1000001):
    if check[i] == 0:
        is_prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

T = int(input())

for _ in range(T):
    cnt = 0
    N = int(input())
    for i in is_prime:
        if i >= N:
            break
        if check[N - i] == 0 and i <= N - i:
            cnt += 1

    print(cnt)