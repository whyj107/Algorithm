# 문제
# Given a Sudoku data structure with size NxN, N > 0
# and √N == integer, write a method to validate if it has been filled out correctly.

# 입력 == 출력
# goodSudoku2 = Sudoku([
#   [1,4, 2,3],
#   [3,2, 4,1],
#
#   [4,1, 3,2],
#   [2,3, 1,4]
# ])
# badSudoku2 = Sudoku([
#   [1,2,3,4,5],
#   [1,2,3,4],
#   [1,2,3,4],
#   [1]
# ])

# My Code
class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.len = max(len(i) for i in self.data)
        self.square_len = int(self.len**0.5)
        self.nums = set(range(1, self.len + 1))

    def is_valid(self):
        # 사이즈 검사
        if False in [len(i) == self.len for i in self.data]:
            return False

        # 데이터 타입 검사
        if False in [True if type(j) == type(1) else False for i in self.data for j in i]:
            return False
    
        # set을 사용하면 순서대로 정렬이 된다. 정렬된 것들과 nums을 비교하여 같으면 True 다르면 False
        # 가로줄 검사
        if False in [set(i) == self.nums for i in self.data]:
            return False

        # 세로줄 검사
        if False in [set(i) == self.nums for i in zip(*self.data)]:
            return False

        # 사각형 검사
        squares = [{self.data[i][j]
                    for i in range(y * self.square_len, y * self.square_len + self.square_len)
                    for j in range(x * self.square_len, x * self.square_len + self.square_len)} == self.nums
                    for x in range(0, self.square_len)
                    for y in range(0, self.square_len)]
        print(squares)
        if False in squares:
            return False

        return True


if __name__=='__main__':
    goodSudoku2 = Sudoku([[1, 4, 2, 3],
                          [3, 2, 4, 1],
                          [4, 1, 3, 2],
                          [2, 3, 1, 4]])
    print(goodSudoku2.is_valid())