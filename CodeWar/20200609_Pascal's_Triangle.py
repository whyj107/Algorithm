# 문제
# Pascal's Triangle
# Write a function that, given a depth (n),
# returns a single-dimensional array/list representing Pascal's Triangle from the first to the n-th level.

# 입력 == 출력
# Test.assert_equals(pascals_triangle(1), [1],"1 level triangle incorrect");
# Test.assert_equals(pascals_triangle(2), [1,1,1],"2 level triangle incorrect");
# Test.assert_equals(pascals_triangle(3), [1,1,1,1,2,1],"3 level triangle incorrect");

# My Code
def pascals_triangle(n):
    pascal = [[1]]
    answer = [1]
    for i in range(n - 1):
        tmp = [1]
        for j in range(len(pascal[i]) - 1):
            tmp.append(pascal[i][j] + pascal[i][j + 1])
        tmp.append(1)
        pascal.append(tmp)
        answer.extend(tmp)
    return answer

# Warriors Code
def pascals_triangle1(n):
    if n == 1:
        return [1]
    prev = pascals_triangle(n - 1)
    return prev + [1 if i == 0 or i == n -1 else prev[-i] + prev[-(i + 1)] for i in range(n)]

if __name__ == '__main__':
    print(pascals_triangle(1), [1], "1 level triangle incorrect");
    print(pascals_triangle(2), [1, 1, 1], "2 level triangle incorrect");
    print(pascals_triangle(3), [1, 1, 1, 1, 2, 1], "3 level triangle incorrect");