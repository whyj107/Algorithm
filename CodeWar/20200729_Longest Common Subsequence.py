# 문제
# Longest Common Subsequence
# https://www.codewars.com/kata/52756e5ad454534f220001ef/train/python

# 나의 풀이
from itertools import combinations
def lcs(x, y):
    x_t = []
    y_t = []
    for i in range(1, len(x)+1):
        x_t.extend(list(map(''.join, combinations(x, i))))
    for i in range(1, len(y)+1):
        y_t.extend(list(map(''.join, combinations(y, i))))

    if len(sorted(set(x_t)&set(y_t), key=lambda x: len(x))) < 1:
        return ""
    else:
        return sorted(set(x_t)&set(y_t), key=lambda x: len(x))[-1]

# 다른 사람의 풀이
def lcs0(x, y):
    if len(x) == 0 or len(y) == 0:
        return ''
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        lcs1 = lcs(x,y[:-1])
        lcs2 = lcs(x[:-1],y)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2

def subsequences(s):
    """Returns set of all subsequences in s."""
    return set(''.join(c) for i in range(len(s) + 1) for c in combinations(s, i))

def lcs1(x, y):
    """Returns longest matching subsequence of two strings."""
    return max(subsequences(x).intersection(subsequences(y)), key=len)

if __name__ == '__main__':
    print(lcs("a", "b"), "")
    print(lcs("abcdef", "abc"), "abc")
    print(lcs( "132535365", "123456789"), "12356")