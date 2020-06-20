# 문제
# 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3#

# 나의 풀이
def solution(board, moves):
    basket = [0]
    answer = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            sero = list(zip(*board))[moves[i] - 1]
            if sero[j] != 0:
                if basket[-1] == sero[j]:
                    del basket[-1]
                    answer += 2
                else:
                    basket.append(sero[j])

                board[j][moves[i] - 1] = 0
                break
    return answer

# 다른 사람의 풀이
def solution1(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer

if __name__ == '__main__':
    print(solution([[0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 3],
                    [0, 2, 5, 0, 1],
                    [4, 2, 4, 4, 2],
                    [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))