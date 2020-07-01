# 문제
# Matrix Addition
# Write a function that accepts two square matrices (N x N two dimensional arrays),
# and return the sum of the two.
# Both matrices being passed into the function will be of size N x N (square),
# containing only integers.
#
# How to sum two matrices:
# Take each cell [n][m] from the first matrix,
# and add it with the same [n][m] cell from the second matrix.
# This will be cell [n][m] of the solution matrix.

# 입력 == 출력
# Test.assert_equals(matrix_addition(
#   [ [1, 2],
#     [1, 2] ],
# #     +
#   [ [2, 3],
#     [2, 3] ] ),
# #     =
#   [ [3, 5],
#     [3, 5] ] )
#
# Test.assert_equals(matrix_addition(
#   [ [1] ],
# #    +
#   [ [2] ] ),
# #    =
#   [ [3] ] )
#
# Test.assert_equals(matrix_addition(
#   [ [1, 2, 3],
#     [3, 2, 1],
#     [1, 1, 1] ],
# #       +
#   [ [2, 2, 1],
#     [3, 2, 3],
#     [1, 1, 3] ] ),
# #       =
#   [ [3, 4, 4],
#     [6, 4, 4],
#     [2, 2, 4] ] )

# My Code
def matrix_addition(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[i]))]for i in range(len(a))]

# Warriors Code
import numpy as np
def matrix_addition1(a, b):
    return(np.mat(a)+np.mat(b)).tolist()

if __name__ == '__main__':
    print(matrix_addition(
        [[1, 2],
         [1, 2]],
        #     +
        [[2, 3],
         [2, 3]]),
        #     =
        [[3, 5],
         [3, 5]])

    print(matrix_addition(
        [[1]],
        #    +
        [[2]]),
        #    =
        [[3]])

    print(matrix_addition(
        [[1, 2, 3],
         [3, 2, 1],
         [1, 1, 1]],
        #       +
        [[2, 2, 1],
         [3, 2, 3],
         [1, 1, 3]]),
        #       =
        [[3, 4, 4],
         [6, 4, 4],
         [2, 2, 4]])