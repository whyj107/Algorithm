# 문제
# 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3

# 나의 풀이
import numpy as np
def solution(arr1, arr2):
    return (np.matrix(arr1) + np.matrix(arr2)).tolist()

# 다른 사람의 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

if __name__ == '__main__':
    print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))