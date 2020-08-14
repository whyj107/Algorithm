# 문제
# Find the Mine!
# https://www.codewars.com/kata/528d9adf0e03778b9e00067e/train/python

# 나의 풀이
def mineLocation(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                return [i, j]

# 다른 사람의 풀이
from numpy import where, array
def mineLocation1(field):
    x, y = where(array(field) == 1)
    return [int(x), int(y)]

if __name__ == '__main__':
    print(mineLocation([[1, 0], [0, 0]]), [0, 0])
    print(mineLocation([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), [0, 0])
    print(mineLocation([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]), [2, 2])