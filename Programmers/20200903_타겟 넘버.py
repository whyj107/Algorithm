# 문제
# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

# 풀이
def solution(numbers, target):
    queue = [0]
    for i in numbers:
        tmp = []
        for j in queue:
            tmp.append(j+i)
            tmp.append(j-i)
        queue = tmp
    return queue.count(target)

# 다른 풀이
from itertools import product
def solution1(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3), 5)