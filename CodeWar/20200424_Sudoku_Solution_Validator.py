# 문제
# Sudoku is a game played on a 9x9 grid.
# The goal of the game is to fill all cells of the grid with digits from 1 to 9,
# so that each column, each row, and each of the nine 3x3 sub-grids
# (also known as blocks) contain all of the digits from 1 to 9.

# 입력 == 출력
# test.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
#                                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
#                                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
#                                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
#                                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
#                                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                                    [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True);
#
# test.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
#                                    [6, 7, 2, 1, 9, 0, 3, 4, 9],
#                                    [1, 0, 0, 3, 4, 2, 5, 6, 0],
#                                    [8, 5, 9, 7, 6, 1, 0, 2, 0],
#                                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                                    [9, 0, 1, 5, 3, 7, 2, 1, 4],
#                                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                                    [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False);

# My Code
def valid_solution(board):
    nums = set(range(1, 10))
    # 가로줄 검사
    if False in [set(i) == nums for i in board]:
        return False

    # 세로줄 검사
    if False in [set(i) == nums for i in zip(*board)]:
        return False

    squares = [{board[i][j]
                for i in range(y * 3, y * 3 + 3)
                for j in range(x * 3, x * 3 + 3)} == nums
                for x in range(0, 3)
                for y in range(0, 3)]
    # 3x3 검사
    if False in squares:
        return False

    return True

if __name__=='__main__':
    print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                          [6, 7, 2, 1, 9, 5, 3, 4, 8],
                          [1, 9, 8, 3, 4, 2, 5, 6, 7],
                          [8, 5, 9, 7, 6, 1, 4, 2, 3],
                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
                          [9, 6, 1, 5, 3, 7, 2, 8, 4],
                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
                          [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
    print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                          [6, 7, 2, 1, 9, 0, 3, 4, 9],
                          [1, 0, 0, 3, 4, 2, 5, 6, 0],
                          [8, 5, 9, 7, 6, 1, 0, 2, 0],
                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
                          [9, 0, 1, 5, 3, 7, 2, 1, 4],
                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
                          [3, 0, 0, 4, 8, 1, 1, 7, 9]]))