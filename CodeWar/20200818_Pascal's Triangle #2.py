# 문제
# Pascal's Triangle #2
# https://www.codewars.com/kata/52945ce49bb38560fe0001d9/train/python

# 나의 풀이
def pascal(p):
    pascal = [[1]]
    for i in range(p - 1):
        tmp = [1]
        for j in range(len(pascal[i]) - 1):
            tmp.append(pascal[i][j] + pascal[i][j + 1])
        tmp.append(1)
        pascal.append(tmp)
    return pascal

# 다른 사람의 풀이
def pascal1(p):
    triangle = [[1]]
    for _ in range(p - 1):
        to_sum = zip([0] + triangle[-1], triangle[-1] + [0])
        triangle.append(list(map(sum, to_sum)))
    return triangle

if __name__ == '__main__':
    print(pascal(1)==[[1]])
    print(pascal1(5)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])