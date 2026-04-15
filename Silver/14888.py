import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_num = -1e9
min_num = 1e9

def dfs(depth, res, plus, minus, multiply, divide):
    global max_num, min_num
    if depth == N:
        max_num = max(res, max_num)
        min_num = min(res, min_num)
        return

    if plus:
        dfs(depth + 1, res + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, res - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, res * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(res / nums[depth]), plus, minus, multiply, divide - 1)

dfs(1, nums[0], oper[0], oper[1], oper[2], oper[3])
print(max_num)  
print(min_num)       
    