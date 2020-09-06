# 뮨제
# 평균구하기
# https://programmers.co.kr/learn/courses/30/lessons/12944?language=python3

# 나의 풀이
def solution(arr):
    return sum(arr)/len(arr)

# 다른 사람의 풀이
from functools import reduce
def average(list):
    return reduce(lambda x, y: x + y, list) / len(list)

if __name__ == '__main__':
    print(solution([1, 2, 3, 4]), 2.5)
    print(solution([5, 5]), 5.0)