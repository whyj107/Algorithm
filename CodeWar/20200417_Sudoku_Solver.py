# 문제
# Write a function that will solve a 9x9 Sudoku puzzle.
# The function will take one argument consisting of the 2D puzzle array,
# with the value 0 representing an unknown square.
# The Sudokus tested against your function will be "easy"
# (i.e. determinable; there will be no need to assume and test possibilities on unknowns)
# and can be solved with a brute-force approach.
# For Sudoku rules, see the Wikipedia article.

# 입력 == 출력
# puzzle = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,0,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,0,2,8,0],
#           [0,0,0,4,1,9,0,0,5],
#           [0,0,0,0,8,0,0,7,9]]
#
# solution = [[5,3,4,6,7,8,9,1,2],
#             [6,7,2,1,9,5,3,4,8],
#             [1,9,8,3,4,2,5,6,7],
#             [8,5,9,7,6,1,4,2,3],
#             [4,2,6,8,5,3,7,9,1],
#             [7,1,3,9,2,4,8,5,6],
#             [9,6,1,5,3,7,2,8,4],
#             [2,8,7,4,1,9,6,3,5],
#             [3,4,5,2,8,6,1,7,9]]

# My Code
zero_index = []
idx = 0
END_FLAG = False

def sudoku(puzzle):
    global zero_index, idx, END_FLAG

    # 반복 실행 막음
    if len(zero_index) < 1:
        # 여러가지 케이스 실행 시 END_FLAG가 True로 있으므로 END_FLAG를 False로 변경
        END_FLAG = False
        # 0인 인덱스만 찾아서 zero_index에 저장
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    zero_index.append([i, j])

    # idx가 zero_index의 길이 만큼 같다면 모두 다 한 것이므로 END_FLAG를 True로 변경
    if idx == len(zero_index):
        END_FLAG = True
        # idx와 zero_index를 초기화
        idx = 0
        zero_index = []
        return puzzle

    # 검증을 통해 숫자를 구함
    a, b = zero_index[idx]
    promise = promising(puzzle, [a, b])

    # 숫자 리스트들을 대입시켜 나가면서 검증
    for p in promise:
        puzzle[a][b] = p
        idx += 1
        sudoku(puzzle)
        # END_FLAG가 True이면 끝
        if END_FLAG:
            return puzzle
    # END_FLAG가 False이면 정답이 아니라는 것으로 원상태로 되돌림
    if END_FLAG == False:
        idx -= 1
        puzzle[a][b] = 0

def promising(puzzle, zero):
    a, b = zero

    # 1 ~ 9까지 숫자 리스트 만듬
    nums = list(map(int, range(1, 10)))

    # 가로 세로 확인
    for i in range(9):
        # 가로 확인하여 리스트에 숫자가 존재하면 지움
        if puzzle[a][i] in nums:
            nums.remove(puzzle[a][i])
        # 세로 확인하여 리스트에 숫자가 존재하면 지움
        if puzzle[i][b] in nums:
            nums.remove(puzzle[i][b])

    # 3x3 확인
    if len(nums) > 0:
        rt = (a // 3) * 3
        ct = (b // 3) * 3
        for i in range(rt, rt + 3):
            for j in range(ct, ct + 3):
                if puzzle[i][j] in nums:
                    nums.remove(puzzle[i][j])
    # 남은 숫자들 리턴
    return nums
# -------------------------------------------------------------------------------------------------
# Warriors Code
from itertools import product

def possibles_(puzzle, x, y):
    a, b = 3*(x/3), 3*(y/3)
    square = set([puzzle[r][c] for r, c in product(range(a, a + 3), range(b, b + 3))])
    row = set(puzzle[x])
    col = set(zip(*puzzle)[y])
    return set(range(1,10)).difference(square.union(row).union(col))

def sudoku_(puzzle):
    z = [(r,c) for (r,c) in product(range(9),range(9)) if puzzle[r][c] == 0]
    if z == []:
        return puzzle
    for (r,c) in z:
        p = possibles_(puzzle, r, c)
        if len(p) == 1:
            puzzle[r][c] = p.pop()
    return sudoku_(puzzle)
# -------------------------------------------------------------------------------------------------
if __name__=='__main__':
    answer = sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                     [6, 0, 0, 1, 9, 5, 0, 0, 0],
                     [0, 9, 8, 0, 0, 0, 0, 6, 0],
                     [8, 0, 0, 0, 6, 0, 0, 0, 3],
                     [4, 0, 0, 8, 0, 3, 0, 0, 1],
                     [7, 0, 0, 0, 2, 0, 0, 0, 6],
                     [0, 6, 0, 0, 0, 0, 2, 8, 0],
                     [0, 0, 0, 4, 1, 9, 0, 0, 5],
                     [0, 0, 0, 0, 8, 0, 0, 7, 9]])
    print(answer)
    puzzle = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 3, 6, 0, 0, 0, 0, 0],
              [0, 7, 0, 0, 9, 0, 2, 0, 0],
              [0, 5, 0, 0, 0, 7, 0, 0, 0],
              [0, 0, 0, 0, 4, 5, 7, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 3, 0],
              [0, 0, 1, 0, 0, 0, 0, 6, 8],
              [0, 0, 8, 5, 0, 0, 0, 1, 0],
              [0, 9, 0, 0, 0, 0, 4, 0, 0]]
    answer = sudoku_(puzzle)
    print(answer)