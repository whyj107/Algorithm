# 문제
# Mean Square Error
# Complete the function that
#
# accepts two integer arrays of equal length
# compares the value each member in one array to the corresponding member in the other
# squares the absolute value difference between those two values
# and returns the average of those squared absolute value difference between each member pair.

# 입력 == 출력
# a1 = [1,2,3]
# a2 = [4,5,6]
# Test.assert_approx_equals(solution(a1, a2), 9)
#
# b1 = [10, 20, 10, 2]
# b2 = [10, 25, 5, -2]
# Test.assert_approx_equals(solution(b1, b2), 16.5)
#
# c1 = [0, -1]
# c2 = [-1, 0]
# Test.assert_approx_equals(solution(c1, c2), 1)
#
# d1 = [10, 10]
# d2 = [10, 10]
# Test.assert_approx_equals(solution(d1, d2), 0)

# My Code
def solution(array_a, array_b):
    return sum([pow(array_a[i] - array_b[i], 2) for i in range(len(array_a))])/len(array_a)

def solution1(a, b):
    return sum((x - y)**2 for x, y in zip(a, b)) / len(a)

if __name__ == '__main__':
    a1 = [1, 2, 3]
    a2 = [4, 5, 6]
    print(solution(a1, a2), 9)

    b1 = [10, 20, 10, 2]
    b2 = [10, 25, 5, -2]
    print(solution(b1, b2), 16.5)

    c1 = [0, -1]
    c2 = [-1, 0]
    print(solution(c1, c2), 1)

    d1 = [10, 10]
    d2 = [10, 10]
    print(solution(d1, d2), 0)