import sys
input = sys.stdin.readline

N = int(input())

chat = set()
cnt = 0

for _ in range(N):
    user = input().strip()
    if user == "ENTER":
        cnt += len(chat)
        chat = set()
    else:
        chat.add(user)

cnt += len(chat)
print(cnt)


