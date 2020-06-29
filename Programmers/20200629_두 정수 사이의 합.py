# 문제
# 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3

# 나의 풀이
def solution(a, b):
    return sum([i for i in range(min(a, b), max(a, b)+1)])

# 다른 사람의 풀이
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

if __name__ == '__main__':
    print(solution(3, 5), 12)
    print(solution(3, 3), 3)
    print(solution(5, 3), 12)