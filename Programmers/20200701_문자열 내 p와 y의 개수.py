# 문제
# 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3

# 나의 문제 풀이
def solution(s):
    return s.lower().count("p") == s.lower().count("y")

if __name__ == '__main__':
    print(solution("pPyY"), True)
    print(solution("Pyy"), False)