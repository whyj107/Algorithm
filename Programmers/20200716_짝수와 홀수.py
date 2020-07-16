# 문제
# 짝수와 훌수
# https://programmers.co.kr/learn/courses/30/lessons/12937?language=python3

# 나의 풀이
def solution(num):
    return "Even" if num%2 == 0 else "Odd"

# 다른 사람의 풀이
def evenOrOdd(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"

if __name__ == '__main__':
    print(solution(2))