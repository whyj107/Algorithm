# 문제
# 서울에서 김서방 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12919?language=python3

# 나의 문제 풀이
def solution(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다"

# 다른 사람의 풀이
def solution1(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

if __name__ == '__main__':
    print(solution(["Jane", "Kim"]), "김서방은 1에 있다")