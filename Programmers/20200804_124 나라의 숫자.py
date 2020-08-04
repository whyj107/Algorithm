# 문제
# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3

# 나의 풀이
def solution(n):
    tmp = ['4', '1', '2']
    answer = tmp[n % 3]
    while n > 3:
        if (n//3)*3 == n:
            n = (n//3)-1
        else:
            n //= 3
        answer += str(tmp[n % 3])
    return answer[::-1]

# 다른사람의 풀이
def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return change124(q) + '124'[r]

if __name__ == '__main__':
    print(solution(1), 1)
    print(solution(2), 2)
    print(solution(3), 4)
    print(solution(4), 11)
    print(solution(5), 12)
    print(solution(6), 14)
    print(solution(7), 21)
    print(solution(8), 22)
    print(solution(9), 24)
    print(solution(10), 41)
    print(solution(11), 42)
    print(solution(12), 44)
    print(solution(13), 111)