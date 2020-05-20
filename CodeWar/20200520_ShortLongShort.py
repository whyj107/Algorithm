# 문제
# Short Long Short
# Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty ( length 0 ).

# 입력 == 출력
# solution("1", "22") # returns "1221"
# solution("22", "1") # returns "1221"

# My Code
def solution(a, b):
    return a + b + a if len(a) < len(b) else b + a + b

if __name__ == '__main__':
    print(solution("1", "22"))
    print(solution("22", "1"))