# 문제
# Substituting Variables Into Strings: Padded Numbers
# Complete the solution so that it returns a formatted string.
# The return value should equal "Value is VALUE" where value is a 5 digit padded number.

# 입력 == 출력
# Test.assert_equals(solution(0), 'Value is 00000')
# Test.assert_equals(solution(5), 'Value is 00005')
# Test.assert_equals(solution(109), 'Value is 00109')
# Test.assert_equals(solution(1204), 'Value is 01204')

# My Code
def solution(value):
    # 1. return 'Value is ' + str(value).zfill(5)
    # 2. return 'Value is %05d'%value
    # 3. return 'Value is {0:05d}'.format(value)
    # 4. return 'Value is ' + format(value, '05')
    return f'Value is {str(value).zfill(5)}'
if __name__ == '__main__':
    print(solution(0), 'Value is 00000')
    print(solution(5), 'Value is 00005')
    print(solution(109), 'Value is 00109')
    print(solution(1204), 'Value is 01204')
