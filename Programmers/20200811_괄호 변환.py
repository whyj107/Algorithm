# 문제
# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3

# 풀이
# 괄호 확인
def check(text):
    tmp = []
    for t in text:
        try:
            if t == '(':
                tmp.append(t)
            else:
                tmp.pop()
        except:
            return False
    return True
# u, v로 문자열 나누기
def divide(p):
    if p == '':
        return ''
    o = 0
    c = 0
    for i in range(len(p)):
        if p[i] == '(':
            o += 1
        else:
            c += 1
        last = p[i]
        if o == c:
            if last == ')':
                return p[:i + 1] + divide(p[i + 1:])
            else:
                return reverse(p[:i + 1], divide(p[i + 1:]))

# 뒤집힌 부분 바로잡기
def reverse(u, v):
    empty = '('
    empty += v + ')'
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            empty += ')'
        else:
            empty += '('
    return empty

def solution(p):
    if check(p):
        return p
    return divide(p)

if __name__ == '__main__':
    print(solution(''), '')
    print(solution("(()())()"), "(()())()")
    print(solution(")("), "()")
    print(solution("()))((()"), "()(())()")