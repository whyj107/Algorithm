# 문제
# 자릿수 더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3

# 나의 풀이
def solution(n):
    return sum(int(i) for i in str(n))

# 다른 사람의 풀이
def sum_digit(number):
    return sum(map(int,str(number)))

if __name__ == '__main__':
    print(solution(123), 6)
    print(solution(987), 24)