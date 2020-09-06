# 문제
# 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3

# 나의 풀이
def solution0(s, n):
    sma = [chr(c) for c in range(ord('a'), ord('z')+1)]
    big = [chr(c) for c in range(ord('A'), ord('Z')+1)]
    return ''.join([i if i == ' ' else (sma[(sma.index(i) + n) % 26] if i in sma else big[(big.index(i) + n) % 26]) for i in s])

import string
def solution(s, n):
    sma = string.ascii_lowercase
    big = string.ascii_uppercase
    return ''.join([i if i == ' ' else (sma[(sma.index(i) + n) % 26] if i in sma else big[(big.index(i) + n) % 26]) for i in s])

# 다른 사람의 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a') + n) % 26 + ord('a'))
    return "".join(s)

if __name__ == '__main__':
    print(solution("AZ", 1) , "BA")
    print(solution("z", 1) , "a")
    print(solution("a B z", 4), "e F d")