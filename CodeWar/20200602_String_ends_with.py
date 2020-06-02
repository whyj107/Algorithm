# 문제
# String ends with?
# Complete the solution so that it returns true
# if the first argument(string) passed in ends with the 2nd argument (also a string).

# 입력 == 출력
# test.assert_equals(solution('abcde', 'cde'), True)
# test.assert_equals(solution('abcde', 'abc'), False)
# test.assert_equals(solution('abcde', ''), True)

# My Code
def solution(string, ending):
    if len(ending) <= len(string):
        for i in range(len(ending)-1, -1, -1):
            if ending[i] != string[i-len(ending)]:
                return False
        return True
    else:
        return False

def solution1(string, ending):
    return string.endswith(ending)

if __name__ == '__main__':
    print(solution1('abcde', 'abc'), False)
    print(solution('abcde', ''), True)