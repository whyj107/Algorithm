# 문제
# Fizz / Buzz
# Write a function that takes an integer and returns an array [A, B, C],
# where A is the number of multiples of 3 (but not 5) below the given integer,
# B is the number of multiples of 5 (but not 3) below the given integer
# and C is the number of multiples of 3 and 5 below the given integer.
#
# For example, solution(20) should return [5, 2, 1]

# 입력 == 출력
# test.assert_equals(solution(20), [5, 2, 1])
# test.assert_equals(solution(2), [0, 0, 0])
# test.assert_equals(solution(14), [4,2,0])
# test.assert_equals(solution(30), [8, 4, 1])
# test.assert_equals(solution(141), [37, 19, 9])

# My Code
def solution(number):
    A = (number - 1) // 3
    B = (number - 1) // 5
    C = (number - 1) // 15
    return [A - C, B - C, C]

if __name__ == '__main__':
    print(solution(20), [5, 2, 1])
    print(solution(2), [0, 0, 0])
    print(solution(14), [4, 2, 0])
    print(solution(30), [8, 4, 1])
    print(solution(141), [37, 19, 9])