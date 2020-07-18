# 문제
# 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940?language=python3

# 나의 풀이
def solution(n, m):
    gc = gcd(n, m)
    return [gc, (n // gc)*(m // gc)*gc]

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

# 다른 사람의 풀이
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 다른 사람의 풀이를 보고 응용
def solution1(n, m):
    gc = gcd(n, m)
    return [gc, n*m//gc]

if __name__ == '__main__':
    print(solution(3, 12), [3, 12])
    print(solution(2, 5), [1, 10])