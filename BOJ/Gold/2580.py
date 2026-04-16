import sys
input = sys.stdin.readline

size = 9
sudoku = []
blank = []

for i in range(size):
    row = list(map(int, input().split()))
    sudoku.append(row)
    for j in range(size):
        if row[j] == 0:
            blank.append((i, j))

def check(r, c, num):

    for i in range(size):
        if sudoku[r][i] == num or sudoku[i][c] == num:
            return False
        
    for i in range(3):
        for j in range(3):
            if sudoku[r//3 * 3 + i][c//3 * 3 + j] == num:
                return False

    return True

def backtracking(idx):
    if idx == len(blank):
        for row in sudoku:
            print(*(row))
        exit(0)

    r, c = blank[idx]
    for num in range(1, 10):
        if check(r, c, num):
            sudoku[r][c] = num
            backtracking(idx + 1)
            sudoku[r][c] = 0

backtracking(0)