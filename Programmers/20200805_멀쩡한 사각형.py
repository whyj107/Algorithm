# 문제
# 멀쩔한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3

# 나의 풀이
def solution(w,h):
    return w*h-(w+h-gcd(w, h))

def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

if __name__ == '__main__':
    print(solution(8, 12), 80)