import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
new_coins = sorted(coins, reverse=True)

ans = 0

for coin in new_coins:
    if K >= coin:
        ans += K // coin
        K %= coin
        if K == 0:
            break

print(ans)
