# 문제
# Reversed Strings
# Complete the solution so that it reverses the string value passed into it.

# 입력 == 출력
# Test.expect(solution('world') == 'dlrow')
# Test.expect(solution('hello') == 'olleh')
# Test.expect(solution('') == '')
# Test.expect(solution('h') == 'h')

# My Code
def solution(string):
    return ''.join([string[i] for i in range(len(string)-1, -1, -1)])

# Warriors Code
def solution1(string):
    return string[::-1]

if __name__=='__main__':
    print(solution('world'))
    print(solution('hello'))
    print(solution(''))
    print(solution('h'))