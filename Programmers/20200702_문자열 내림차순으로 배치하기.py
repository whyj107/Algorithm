# 문제
# 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3

# 나의 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))

if __name__ == '__main__':
    print(solution("Zbcdefg") == "gfedcbZ")