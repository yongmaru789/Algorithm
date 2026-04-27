def quadtree(arr, x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[x][y] != arr[i][j]:
                n = n // 2
                quadtree(arr, x, y, n)
                quadtree(arr, x + n, y, n)
                quadtree(arr, x, y + n, n)
                quadtree(arr, x + n, y + n, n)
                return
            
    # 영역 내 모든 숫자가 같은 값이면, 해당 숫자(0 또는 1)의 개수를 +1
    answer[arr[x][y]] += 1 

def solution(arr):
    global answer
    answer = [0, 0]
    quadtree(arr, 0, 0, len(arr))
    
    # answer[0]은 최종적으로 남은 0의 개수, answer[1]은 최종적으로 남은 1의 개수를 의미한다.
    return answer
