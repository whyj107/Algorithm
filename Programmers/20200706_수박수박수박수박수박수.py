# 문제
# 수박수박수박수박수박수?
# https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3

# 나의 풀이
def solution(n):
    return ''.join(["수" if i%2 == 0 else "박" for i in range(n)])

# 다른 사람의 풀이
def solution1(n):
    return ("수박"*n)[:n]

if __name__ == '__main__':
    print(solution(3), "수박수")
    print(solution1(4), "수박수박")