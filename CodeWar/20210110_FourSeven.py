# Four/Seven
# https://www.codewars.com/kata/5ff50f64c0afc50008861bf0/train/python

# default 값을 주려면
# {4: 7, 7: 4}.get(n, 0)
# 이렇게 사용하면 된다.

# 나의 풀이
def solution(n):
    return {4: 7, 7: 4}.get(n)

# 다른 사람의 풀이
def solution1(n):
    return 4 * (n == 7) + 7 * (n == 4)

def solution2(n):
    return n == 4 and 7 or n == 7 and 4

print(solution(7), 4)
print(solution(4), 7)
print(solution(46), None)