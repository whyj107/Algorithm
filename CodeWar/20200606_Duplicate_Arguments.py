# 문제
# Duplicate Arguments
# Complete the solution so that it returns true if it contains any duplicate argument values.
# Any number of arguments may be passed into the function.
#
# The array values passed in will only be strings or numbers.
# The only valid return values are true and false.

# 입력 == 출력
# Test.assert_equals(solution(1, 2, 3, 1, 2), True)
# Test.assert_equals(solution(1, 1), True)
# Test.assert_equals(solution(1, 0), False)
# Test.assert_equals(solution(1, 0, 2, 3, 4), False)
# Test.assert_equals(solution(), False)

# My Code
def solution(*arg):
    for i in range(len(arg)):
        for j in range(i):
            if arg[i] == arg[j]:
                return True
    return False

# Warriors Code
def solution1(*args):
    return len(args) != len(set(args))

if __name__ == '__main__':
    print(solution(1, 2, 3, 1, 2), True)
    print(solution(1, 1), True)
    print(solution(1, 0), False)
    print(solution(1, 0, 2, 3, 4), False)
    print(solution(), False)