import sys
sys.setrecursionlimit(10 ** 6)

def preorder(arrY, arrX, answer):
    # 현재 서브트리에서 y좌표가 가장 큰 노드를 root로 설정한다.
    node = arrY[0]
    idx = arrX.index(node)
    arrY1 = []
    arrY2 = []
    
    # root를 제외한 나머지 노드들을 x좌표 기준으로 분류한다.
    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])
    
    answer.append(node[2])
    # 왼쪽 서브트리에서 다시 preorder
    if len(arrY1) > 0: 
        preorder(arrY1, arrX[:idx], answer)
    # 오른쪽 서브트리에서 다시 preorder
    if len(arrY2) > 0:
        preorder(arrY2, arrX[idx + 1:], answer)
    return


def postorder(arrY, arrX, answer):
    # 현재 서브트리에서 y좌표가 가장 큰 노드를 root로 설정한다.
    node = arrY[0]
    idx = arrX.index(node)
    arrY1 = []
    arrY2 = []
    
    # root를 제외한 나머지 노드들을 x좌표 기준으로 분류한다.
    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])
            
    # 왼쪽 서브트리에서 다시 postorder
    if len(arrY1) > 0:
        postorder(arrY1, arrX[:idx], answer)
    # 오른쪽 서브트리에서 다시 postorder
    if len(arrY2) > 0:
        postorder(arrY2, arrX[idx + 1:], answer)
    answer.append(node[2])
    return


def solution(nodeinfo):
    preanswer = []
    postanswer = []
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
        
    # 트리의 레벨 순서대로 노드를 탐색하기 위해 Y좌표는 내림차순으로, X좌표는 오름차순으로 정렬
    arrY = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    # 왼쪽/오른쪽 서브트리 경계를 나누는 기준점 역할을 한다. X좌표를 오름차순으로 정렬
    arrX = sorted(nodeinfo)
    
    preorder(arrY, arrX, preanswer)
    postorder(arrY, arrX, postanswer)
    
    return [preanswer, postanswer]