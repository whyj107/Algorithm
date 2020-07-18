# 문제
# 자연수 뒤집어 배열로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3

# 나의 문제 풀이
def solution(n):
    return [int(i) for i in str(n)[::-1]]

# 다른 사람의 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

if __name__ == '__main__':
    print(solution(12345), [5, 4, 3, 2, 1])