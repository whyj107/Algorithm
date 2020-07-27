# 문제
# x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954?language=python3

# 나의 풀이
def solution(x, n):
    return [x*i for i in range(1, n+1)]

if __name__ == '__main__':
    print(solution(2, 5), [2, 4, 6, 8, 10])
    print(solution(-4, 2), [-4, -8])