# Simple string matching
# https://www.codewars.com/kata/5bc052f93f43de7054000188/train/python

# 나의 풀이
def solve(a, b):
    if a.count('*') > 0:
        a = a.split('*')
        if len(a[0]+a[1]) > len(b):
            return False
        return True if b.startswith(a[0]) and b.endswith(a[1]) else False
    else:
        return True if a == b else False

# 다른 사람의 풀이
from fnmatch import fnmatch
def solve1(a, b):
    return fnmatch(b, a)

import re
def solve2(a,b):
    return bool(re.fullmatch(a.replace('*', '.*'), b))

def solve3(a, b):
    return bool(re.match(f"^{a.replace('*', '.*')}$", b))

# print(solve("code*s", "codewars"), True)
# print(solve("codewar*s", "codewars"), True)
# print(solve("code*warrior", "codewars"), False)
# print(solve("c", "c"), True)
# print(solve("*s", "codewars"), True)
# print(solve("*s", "s"), True)
print(solve("s*", "s"), True)
# print(solve("aa", "aaa"), False)
# print(solve("aa*", "aaa"), True)
# print(solve("aaa", "aa"), False)
# print(solve("aaa*", "aa"), False)
# print(solve("*", "codewars"),True)
print(solve("aaa*aaa", "aaa"), False)