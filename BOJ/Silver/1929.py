import sys
input = sys.stdin.readline
import math

M, N = map(int, input().split())

def is_Prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for i in range(M, N + 1):
    if is_Prime(i):
        print(i)