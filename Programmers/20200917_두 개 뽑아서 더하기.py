# 문제
# 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

# 나의 풀이
from itertools import combinations
def solution(numbers):
    answer = []
    for i in combinations(numbers, 2):
        answer.append(sum(i))
    answer = sorted(list(set(answer)))
    return answer

# 다른 사람의 풀이
def solution1(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))