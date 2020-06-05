# 문제
# Break camelCase
# Complete the solution so that the function will break up camel casing,
# using a space between words.

# 입력 == 출력
# Test.assert_equals(solution("helloWorld"), "hello World")
# Test.assert_equals(solution("camelCase"), "camel Case")
# Test.assert_equals(solution("breakCamelCase"), "break Camel Case")

def solution(s):
    tmp = ""
    for i in s:
        if i == i.upper():
            tmp += ' '
        tmp += i
    return tmp

def solution1(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

if __name__ == '__main__':
    print(solution("helloWorld"), "hello World")
    print(solution("camelCase"), "camel Case")
    print(solution("breakCamelCase"), "break Camel Case")
