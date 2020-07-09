# 문제
# 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3

# 나의 풀이
def solution(n):
    return sum([i for i in range(1, n+1) if n%i == 0])

# 다른 사람의 풀이
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

if __name__ == '__main__':
    print(solution(12), 28)
    print(solution(5), 6)