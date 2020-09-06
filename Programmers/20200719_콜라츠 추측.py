# 문제
# 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943?language=python3

# 나의 풀이
def solution0(num):
    cnt = 0
    while num != 1:
        if num%2 == 0:
            num /= 2
        else:
            num = (num*3+1)
        cnt += 1
        if cnt > 500:
            return -1
    return cnt
# upgrade
def solution(num):
    cnt = 0
    while num != 1:
        num = num /2 if num%2 == 0 else num*3 + 1
        cnt += 1
        if cnt > 500: return -1
    return cnt


# 다른 사람의 풀이
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1

if __name__ == '__main__':
    print(solution(6), 8)
    print(solution(16), 4)
    print(solution(626331), -1)