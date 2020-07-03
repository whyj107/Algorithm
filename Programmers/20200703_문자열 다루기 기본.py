# 문제
# 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3

# 나의 풀이
def solution(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)

# 다른 사람의 풀이
def solution1(s):
    return s.isdigit() and len(s) in [4, 6]

if __name__ == '__main__':
    print(solution('1234'), True)
    print(solution('12345'), False)
    print(solution('a1234'), False)