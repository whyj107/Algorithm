# Simple string reversal
# https://www.codewars.com/kata/5a71939d373c2e634200008e/train/python

# 나의 풀이
def solve(s):
    s_tmp = list(s[::-1].replace(' ', ''))
    return ''.join(' ' if i == ' ' else s_tmp.pop(0) for i in s)

# 다른 사람의 풀이
def solve2(s):
    it = reversed(s.replace(' ',''))
    return ''.join(c if c == ' ' else next(it) for c in s)

print(solve("codewars"), "srawedoc")
print(solve("your code"), "edoc ruoy")
print(solve("your code rocks"), "skco redo cruoy")
print(solve("i love codewars"), "s rawe docevoli")