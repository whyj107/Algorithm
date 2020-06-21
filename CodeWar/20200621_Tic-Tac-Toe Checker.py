# 문제
# Tic-Tac-Toe Checker
# If we were to set up a Tic-Tac-Toe game,
# we would want to know whether the board's current state is solved, wouldn't we?
# Our goal is to create a function that will check that for us!
#
# Assume that the board comes in the form of a 3x3 array,
# where the value is 0 if a spot is empty,
# 1 if it is an "X", or 2 if it is an "O", like so:

# 입력 == 출력
# # not yet finished
# board = [[0, 0, 1],
#          [0, 1, 2],
#          [2, 1, 0]]
# test.assert_equals(is_solved(board), -1)
#
# # winning row
# board = [[1, 1, 1],
#          [0, 2, 2],
#          [0, 0, 0]]
# test.assert_equals(is_solved(board), 1)
#
# # winning column
# board = [[2, 1, 2],
#          [2, 1, 1],
#          [1, 1, 2]]
# test.assert_equals(is_solved(board), 1)
#
# # draw
# board = [[2, 1, 2],
#          [2, 1, 1],
#          [1, 2, 1]]
# test.assert_equals(is_solved(board), 0)

# My Code
def is_solved(board):
    # 가로
    for i in board:
        if len(set(i)) == 1 and list(set(i))[0] != 0:
            return i[0]

    # 세로
    for i in zip(*board):
        if len(set(i)) == 1 and list(set(i))[0] != 0:
            return i[0]

    # 대각선
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] != 0:
            return board[1][1]

    # 0이 존재하면 아직 안 끝난 것
    for i in board:
        if i.count(0) != 0:
            return -1

    # 0이 존재하지 않으면 비긴 것
    return 0

if __name__ == '__main__':
    # not yet finished
    board = [[0, 0, 1],
             [0, 1, 2],
             [2, 1, 0]]
    print(is_solved(board), -1)

    # winning row
    board = [[1, 1, 1],
             [0, 2, 2],
             [0, 0, 0]]
    print(is_solved(board), 1)

    # winning column
    board = [[2, 1, 2],
             [2, 1, 1],
             [1, 1, 2]]
    print(is_solved(board), 1)

    # draw
    board = [[2, 1, 2],
             [2, 1, 1],
             [1, 2, 1]]
    print(is_solved(board), 0)