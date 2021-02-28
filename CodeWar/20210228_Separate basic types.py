# Separate basic types
# https://www.codewars.com/kata/60113ded99cef9000e309be3/train/python

# 나의 풀이
def separate_types(seq):
    dict = {}
    for i in seq:
        if not type(i) in dict:
            dict[type(i)] = [i]
        else:
            dict[type(i)].append(i)
    return dict

# 다른 사람의 풀이
from collections import defaultdict
def separate_types1(seq):
    D = defaultdict(list)
    for x in seq:
        D[type(x)].append(x)
    return D

def separate_types2(seq):
    i, s, b = [], [], []
    res = {int: i, str: s, bool: b}
    for x in seq:
        if type(x) == str: s.append(x)
        elif type(x) == int: i.append(x)
        else: b.append(x)
    if not i: res.pop(int)
    if not b: res.pop(bool)
    if not s: res.pop(str)
    return res

print(separate_types(['a', 1, 2, False, 'b']), {int: [1, 2], str: ['a', 'b'], bool: [False]})
print(separate_types(['a', 1, 2]), {int: [1, 2], str: ['a']})