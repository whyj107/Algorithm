import sys
sudoku = []
zero = []
S_SIZE = 9
Z_SIZE = 0
END_FLAG = False

for i in range(S_SIZE):
    sudoku.append(sys.stdin.readline().split())
    for j in range(S_SIZE):
        if sudoku[i][j] == '0':
            zero.append([i, j])
            Z_SIZE += 1

def get_possible(zero):
    a, b = zero
    nums = list(map(str, range(1, 10)))
    for i in range(S_SIZE):
        if sudoku[a][i] in nums:
            nums.remove(sudoku[a][i])
        if sudoku[i][b] in nums:
            nums.remove(sudoku[i][b])

    if len(nums) > 0:
        rt = (a // 3) * 3
        ct = (b // 3) * 3

        for i in range(rt, rt+3):
            for j in range(ct, ct+3):
                if sudoku[i][j] in nums:
                    nums.remove(sudoku[i][j])

    return nums

def solve(idx):
    if idx == Z_SIZE:
        global END_FLAG
        END_FLAG = True
        return

    global sudoku
    a, b = zero[idx]
    possible = get_possible(zero[idx])

    for p in possible:
        sudoku[a][b] = p
        solve(idx+1)
        if END_FLAG:
            return

    if END_FLAG == False:
        sudoku[a][b] = '0'

solve(0)

for s in sudoku:
    print(' '.join(s))