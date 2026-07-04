import sys
input = sys.stdin.readline
import math

max = 123456
is_prime = [True] * (max*2 + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, max*2 + 1):
    if is_prime[i]:
        for j in range(i * 2, max*2 + 1, i):
            is_prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(is_prime[n + 1 : n*2 + 1]))
