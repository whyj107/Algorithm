# Limit string length - 1
# https://www.codewars.com/kata/5208fc3cb613bc725f000142/train/python

# 나의 풀이
def solution(st, limit):
    return st[:limit] + "..." if len(st) > limit else st

# 다른 사람의 풀이
def solution1(st, limit):
    return f'{st[:limit]}{"..." * (len(st) > limit)}'

print(solution('Testing String',3), 'Tes...')
print(solution('Testing String',8), 'Testing ...')
print(solution('Test', 10), 'Test')
print(solution('Test', 4), 'Test')