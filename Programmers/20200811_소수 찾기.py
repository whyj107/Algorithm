# 문제
# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

# 나의 풀이
def solution(numbers):
    import itertools
    answer = 0
    n = [i for i in numbers]
    tmp = []
    for i in range(1, len(numbers)+1):
        tmp.extend(list(map(int, map(''.join, itertools.permutations(n, i)))))
    tmp = list(set(tmp))
    for j in tmp:
        if is_prime(int(j)):
            answer += 1
    return answer

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, round(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# 다른 사람의 풀이
def solution1(n):
    from itertools import permutations
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

if __name__ == '__main__':
    print(solution("17"), 3)
    print(solution("011"), 2)