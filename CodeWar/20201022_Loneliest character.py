# Loneliest character
# https://www.codewars.com/kata/5f885fa9f130ea00207c7dc8/train/python

# 나의 풀이
def loneliest(strng):
    strng = strng.lstrip().rstrip()
    d = {}
    pre, l, r = strng[0], 0, 0
    for i in range(1, len(strng)):
        if strng[i] == ' ':
            r += 1
        else:
            if not d.get(l+r):
                d[l+r] = []
            d[l+r].append(pre)
            l, r, pre = r, 0, strng[i]

    if not d.get(l + r):
        d[l + r] = []
    d[l + r].append(pre)
    return d[max(d.keys())]

# 다른 사람의 풀이
def loneliest1(s):
    s = s.strip()
    ind = [-1, len(s)]
    for i in range(len(s)):
        if s[i] != ' ':
            ind.insert(-1, i)

    d = {}
    for i in range(1, len(ind) - 1):
        x = ind[i + 1] - ind[i - 1] - 2
        if not d.get(x):
            d[x] = []
        d[x].append(s[ind[i]])
    return (d[max(d)])

print(sorted(loneliest('a')), ['a'])
print(sorted(loneliest('abc d   ef  g   h i j      ')), ['g'])
print(sorted(loneliest('a   b   c ')), ['b'])
print(sorted(loneliest('  abc  d  z    f gk s ')), ['z'])
print(sorted(loneliest('a  b  c  de  ')), ['b', 'c'])
print(sorted(loneliest('abc')), ['a', 'b', 'c'])