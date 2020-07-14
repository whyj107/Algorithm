# 문제
# 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3

# 나의 풀이
def solution(n):
    return (int(n**0.5)+1)**2 if n**0.5 == int(n**0.5) else -1

if __name__ == '__main__':
    print(solution(121), 144)
    print(solution(3), -1)