# 문제
# Square Matrix Multiplication
# rite a function that accepts two square (NxN) matrices (two dimensional arrays),
# and returns the product of the two. Only square matrices will be given.
# How to multiply two square matrices:
# We are given two matrices, A and B, of size 2x2 (note: tests are not limited to 2x2).
# Matrix C, the solution, will be equal to the product of A and B.
# To fill in cell [0][0] of matrix C, you need to compute: A[0][0] * B[0][0] + A[0][1] * B[1][0].
# More general:
# To fill in cell [n][m] of matrix C,
# you need to first multiply the elements in the nth row of matrix A by the elements in the mth column of matrix B,
# then take the sum of all those products.
# This will give you the value for cell [m][n] in matrix C.

# 입력 == 출력
# Test.assert_equals(matrix_mult(
#   [ [1, 2],
#     [3, 2] ],
# #      x
#   [ [3, 2],
#     [1, 1] ]),
# #      =
#   [ [5, 4],
#     [11, 8] ])
#
# Test.assert_equals(matrix_mult(
#   [ [9, 7],
#     [0, 1] ],
# #      x
#   [ [1, 1],
#     [4, 12] ]),
# #      =
#   [ [37, 93],
#     [4, 12] ])
#
# Test.assert_equals(matrix_mult(
#   [ [1, 2, 3],
#     [3, 2, 1],
#     [2, 1, 3] ],
# #       x
#   [ [4, 5, 6],
#     [6, 5, 4],
#     [4, 6, 5] ]),
# #        =
#   [ [28, 33, 29],
#     [28, 31, 31],
#     [26, 33, 31] ])

# My Code
def matrix_mult(a, b):
    return [[sum(i*j for i, j in zip(a_row, b_col)) for b_col in zip(*b)] for a_row in a]

import numpy as np
def matrix_mult1(a, b):
    return (np.matrix(a) * np.matrix(b)).tolist()

# Warriors Code
def matrix_mult2(a, b):
  return np.dot(a,b).tolist()

if __name__ == '__main__':
    print(matrix_mult1(
        [[1, 2],
         [3, 2]],
        #      x
        [[3, 2],
         [1, 1]]),
        #      =
        [[5, 4],
         [11, 8]])

    print(matrix_mult(
        [[9, 7],
         [0, 1]],
        #      x
        [[1, 1],
         [4, 12]]),
        #      =
        [[37, 93],
         [4, 12]])

    print(matrix_mult(
        [[1, 2, 3],
         [3, 2, 1],
         [2, 1, 3]],
        #       x
        [[4, 5, 6],
         [6, 5, 4],
         [4, 6, 5]]),
        #        =
        [[28, 33, 29],
         [28, 31, 31],
         [26, 33, 31]])
