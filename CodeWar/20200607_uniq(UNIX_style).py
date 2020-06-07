# 문제
# uniq (UNIX style)
# Implement a function which behaves like the uniq command in UNIX.
#
# It takes as input a sequence
# and returns a sequence in which all duplicate elements following each other have been reduced to one instance.

# 입력 == 출력
# test.assert_equals(uniq(['a','a','b','b','c','a','b','c','c']), ['a','b','c','a','b','c'])
# test.assert_equals(uniq(['a','a','a','b','b','b','c','c','c']), ['a','b','c'])
# test.assert_equals(uniq([]), [])
# test.assert_equals(uniq(['foo']), ['foo'])
# test.assert_equals(uniq(['bar']), ['bar'])
# test.assert_equals(uniq(['']), [''])
# test.assert_equals(uniq([None,'a','a']), [None,'a'])

# My Code
def uniq(seq):
    pre = 'first'
    answer = []
    for i in seq:
        if pre == i:
            continue
        pre = i
        answer.append(i)
    return answer

# Warriors Code
from itertools import groupby
def uniq1(seq):
    return [k for k,_ in groupby(seq)]

if __name__ == '__main__':
    print(uniq(['a', 'a', 'b', 'b', 'c', 'a', 'b', 'c', 'c']), ['a', 'b', 'c', 'a', 'b', 'c'])
    print(uniq(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']), ['a', 'b', 'c'])
    print(uniq([]), [])
    print(uniq(['foo']), ['foo'])
    print(uniq(['bar']), ['bar'])
    print(uniq(['']), [''])
    print(uniq([None, 'a', 'a']), [None, 'a'])