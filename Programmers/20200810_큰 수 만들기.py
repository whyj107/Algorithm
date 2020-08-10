# 문제
# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

# 나의 풀이
# 시간 초과
import itertools
def solution0(number, k):
    n = [i for i in number]
    return max(list(map(''.join, itertools.combinations(n, len(n)-k))))

def solution(number, k):
    a = [number[0]]
    for i in number[1:]:
        while len(a) > 0 and a[-1] < i and k > 0:
            k -= 1
            a.pop()
        a.append(i)
    if k != 0:
        a = a[:-k]
    return ''.join(a)


if __name__ == '__main__':
    print(solution("1924", 2), "94")
    print(solution("1231234", 3), "3234")
    print(solution("4177252841", 4), "775841")