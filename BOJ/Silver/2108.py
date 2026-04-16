import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

res1 = round(sum(nums) / N)


nums.sort()
res2 = nums[N//2]


cnt = dict()
for i in nums:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

mx = max(cnt.values())
mx_dic = []
for i in cnt:
    if mx == cnt[i]:
        mx_dic.append(i)

if len(mx_dic) > 1:
    res3 = mx_dic[1]
else:
    res3 = mx_dic[0]


res4 = max(nums) - min(nums)


print(res1)
print(res2)
print(res3)
print(res4)
