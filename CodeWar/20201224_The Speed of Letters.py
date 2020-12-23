# The Speed of Letters
# https://www.codewars.com/kata/5fc7caa854783c002196f2cb/train/python

# 문제를 파악하기 힘든 문제이다.
# 다른 사람의 풀이
def speedify(s):
    lst = [' '] * (len(s)+26)
    for i, c in enumerate(s):
        lst[i+ord(c)-65] = c
    return ''.join(lst).rstrip()

def speedify1(st):
    ans = [' ']  * len(st) * 26
    for i, c in enumerate(st):
        gap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c)
        ans[gap + i] = c
    return ''.join(ans).rstrip()

print(speedify("AZ"), "A                         Z")
print(speedify("ABC"), "A B C")
print(speedify("ACE"), "A  C  E")
print(speedify("CBA"), "  A")
print(speedify("HELLOWORLD"), "     E H    DLL   OLO   R  W")