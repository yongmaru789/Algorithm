import sys
input = sys.stdin.readline

def fib():
    N = int(input())

    if N == 1:
        return 1
    if N == 2:
        return 2
    
    a, b = 1, 2
    for i in range(3, N + 1):
        a, b = b, (a + b) % 15746
    
    return b

print(fib())
