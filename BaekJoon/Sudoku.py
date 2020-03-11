# 가로 체크
def horizontal(x, val):
    if val in sudoku[x]:
        return False
    return True

# 세로 체크
def vertical(y, val):
    for i in range(9):
        if val == sudoku[i][y]:
            return False
    return True

# 3x3 체크
def threebythree(x, y, val):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[nx+i][ny+i]:
                return False
    return True

def dfs1(index):
    if index == len(zeros):
        for row in sudoku:
            for n in row:
                print(n, end=" ")
            print()
        return
    else:
        for i in range(1, 10):
            nx = zeros[index][0]
            ny = zeros[index][1]

            if horizontal(nx, i) and vertical(ny, i) and threebythree(nx, ny, i):
                sudoku[nx][ny] = i
                dfs1(index + 1)
                sudoku[nx][ny] = 0

if __name__=='__main__':
    global sudoku, zeros

    sudoku = []

    flag = False

    for n in range(9):
        sudoku.append(list(map(int, input().split())))

    zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

    dfs1(0)