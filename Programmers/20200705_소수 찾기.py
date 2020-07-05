# 문제
# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

# 나의 풀이
def solution(n):
    num = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)

if __name__ == '__main__':
    print(solution(10), 4)
    print(solution(5), 3)
    print(solution(2), 1)