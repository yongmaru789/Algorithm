import sys
input = sys.stdin.readline

N = int(input())
front = list(map(int, input().split()))
st = []
number = 1

for i in front:
    st.append(i)
    while st and st[-1] == number:
        st.pop()
        number += 1

if len(st) == 0:
    print("Nice")
else:
    print("Sad")