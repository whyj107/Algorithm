# 문제
# 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3

# 나의 풀이
def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0

# 다른 사람의 풀이
def Harshad(n):
    return not(n % sum([int(x) for x in str(n)]))

if __name__ == '__main__':
    print(solution(10), True)
    print(solution(12), True)
    print(solution(11), False)
    print(solution(13), False)
