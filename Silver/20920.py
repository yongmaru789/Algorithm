import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
words = [input().strip() for _ in range(N)]

new_words = [w for w in words if len(w) >= M]

cnt = Counter(new_words)
unique_words = cnt.keys()

result = sorted(unique_words, key=lambda x: (-cnt[x], -len(x), x))

for word in result:
    print(word)

