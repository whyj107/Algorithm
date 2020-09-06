# 문제
# 문자열을 정수로 바꾸기
# https://programmers.co.kr/learn/courses/30/lessons/12925?language=python3

# 나이 풀이
def solution(s):
    return int(s)

# 다른 사람의 풀이
def strToInt(str):
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-': result *= -1
        else: result += int(number) * (10 ** idx)
    return result

if __name__ == '__main__':
    print(solution("1234"), 1234)
    print(strToInt("-1234"), -1234)