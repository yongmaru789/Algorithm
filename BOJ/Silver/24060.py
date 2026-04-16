import sys
input = sys.stdin.readline

def mergesort(left, right):
    if left < right :
        m = (left + right) // 2
        mergesort(left, m)
        mergesort(m+1, right)
        merge(left, m, right)

def merge(left, m, right):
    i = left
    j = m + 1
    t = left

    while (i <= m and j <= right):
        if (A[i] <= A[j]):
            result.append(A[i])
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            result.append(A[j])
            tmp[t] = A[j]
            t += 1
            j += 1
    
    while i <= m:
        result.append(A[i])
        tmp[t] = A[i]
        t += 1
        i += 1
    while j <= right:
        result.append(A[j])
        tmp[t] = A[j]
        t += 1
        j += 1

    i = left
    t = left
    while i <= right:
        A[i] = tmp[t]
        i += 1
        t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))

tmp = list(0 for _ in range(N))
result = list()

mergesort(0, N-1)
if K <= len(result):
    print(result[K-1])
else:
    print(-1)

