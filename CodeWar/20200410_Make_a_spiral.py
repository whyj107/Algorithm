# 문제
# Your task, is to create a NxN spiral with a given size.
# For example, spiral with size 5 should look like this:
# 00000
# ....0
# 000.0
# 0...0
# 00000
# and with the size 10:
# 0000000000
# .........0
# 00000000.0
# 0......0.0
# 0.0000.0.0
# 0.0..0.0.0
# 0.0....0.0
# 0.000000.0
# 0........0
# 0000000000
# Return value should contain array of arrays, of 0 and 1,
# for example for given size 5 result should be:
# [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Because of the edge-cases for tiny spirals, the size will be at least 5.
# General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.

# 입력 == 출력
# Test.assert_equals(spiralize(5), [[1,1,1,1,1],
#                                   [0,0,0,0,1],
#                                   [1,1,1,0,1],
#                                   [1,0,0,0,1],
#                                   [1,1,1,1,1]])
# Test.assert_equals(spiralize(8), [[1,1,1,1,1,1,1,1],
#                                   [0,0,0,0,0,0,0,1],
#                                   [1,1,1,1,1,1,0,1],
#                                   [1,0,0,0,0,1,0,1],
#                                   [1,0,1,0,0,1,0,1],
#                                   [1,0,1,1,1,1,0,1],
#                                   [1,0,0,0,0,0,0,1],
#                                   [1,1,1,1,1,1,1,1]])

# My Code
def spiralize(size):
    # spiral 리스트에 전부 0으로 초기화
    spiral = [[0] * size] * size
    # 맨 첫 줄을 1로 변경
    spiral[0] = [1] * size
    # list[i][j]를 풀기 위한 변수들
    # index가 i에 해당되고 start와 end는 j의 범위
    index = 0
    start = 0
    end = size

    # 맨 첫 줄을 제외하고 돌려가면서 값 변경
    for i in range(1, size):
        spiral = list(map(list, zip(*spiral)))[::-1]
        for j in range(start, end):
            spiral[index][j] = 1
        if i % 4 == 3:
            index += 2
        elif i % 4 == 0:
            start += 2
        elif i % 4 == 2:
            end -= 2

    # 회전 시키면서 값을 바꿨기 때문에 원래 자리로 돌리기 위해서 남은 회전을 해줌
    for i in range(5, size % 4, -1):
        spiral = list(map(list, zip(*spiral)))[::-1]

    return spiral

# 출력 예쁘게 보려고 pprint 사용
from pprint import pprint
if __name__=='__main__':
    answer = spiralize(5)
    pprint(answer)
    answer = spiralize(8)
    pprint(answer)
    answer = spiralize(11)
    pprint(answer)
    answer = spiralize(14)
    pprint(answer)