# 문제
# uniq -c (UNIX style)
# Implement a function which behaves like the 'uniq -c' command in UNIX.
#
# It takes as input a sequence and returns a sequence in which all duplicate elements following
# each other have been reduced to one instance together with the number of times a duplicate elements occurred in the original array.

# 입력 == 출력
# test.assert_equals(uniq_c(['a','a','b','b','c','a','b','c']), [('a',2),('b',2),('c',1),('a',1),('b',1),('c',1)])
# test.assert_equals(uniq_c(['a','a','a','b','b','b','c','c','c']), [('a',3),('b',3),('c',3)])
# test.assert_equals(uniq_c([None,'a','a']), [(None, 1),('a', 2)])
# test.assert_equals(uniq_c(['foo']), [('foo', 1)])
# test.assert_equals(uniq_c(['']), [('', 1)])
# test.assert_equals(uniq_c([]), [])

# My Code
def uniq_c(seq):
    seq += ' '
    answer = []
    cnt = 1
    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            cnt += 1
            continue
        answer.append((seq[i], cnt))
        cnt = 1
    return answer

# Warriors Code
from itertools import groupby
def uniq_c1(seq):
    return [(k,sum(1 for _ in g)) for k, g in groupby(seq)]

def uniq_c2(s):
    lst = []
    c = 1
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            lst.append((s[i],c))
            c = 1
        else:
            c += 1
    if s:
        lst.append((s[-1],c))
    return lst

if __name__ == '__main__':
    print(uniq_c(['a', 'a', 'b', 'b', 'c', 'a', 'b', 'c']),
                [('a', 2), ('b', 2), ('c', 1), ('a', 1), ('b', 1), ('c', 1)])
    print(uniq_c(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']), [('a', 3), ('b', 3), ('c', 3)])
    print(uniq_c([None, 'a', 'a']), [(None, 1), ('a', 2)])
    print(uniq_c(['foo']), [('foo', 1)])
    print(uniq_c(['']), [('', 1)])
    print(uniq_c([]), [])