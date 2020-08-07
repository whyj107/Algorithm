# 문제
# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

# 나의 풀이
# 시간 초과
from itertools import permutations
def solution0(numbers):
    tmp = [''.join(list(map(str, i))) for i in list(permutations(numbers, len(numbers)))]
    tmp.sort()
    return tmp[-1]

# string 비교 문제 풀이
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# 정렬로 문제 풀이
def solution1(numbers):
    numbers = list(map(str, numbers))
    answer = "".join(sorted(numbers, key=lambda x: (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]),reverse=True))
    return answer if int(answer) != 0 else "0"

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2))
def solution2(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

if __name__ == '__main__':
    print(solution([6, 10, 2]), "6210")