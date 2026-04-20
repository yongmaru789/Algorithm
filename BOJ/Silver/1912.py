import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

maximum = [0] * n 
maximum[0] = nums[0]

for i in range(1, n):
    maximum[i] = max(nums[i], nums[i] + maximum[i-1])
print(max(maximum))