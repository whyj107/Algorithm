# 문제
# The reject() function
# https://www.codewars.com/kata/52988f3f7edba9839c00037d/train/python

# 나의 풀이
def reject(seq, predicate):
    return [i for i in seq if not predicate(i)]

# 다른 사람의 풀이
def reject1(seq, predicate):
    from itertools import filterfalse
    return list(filterfalse(predicate,seq))

if __name__ == '__main__':
    print(reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0), [1, 3, 5])
    print(reject(['a', 'b', 3, 'd'], lambda x: type(x) == int), ['a', 'b', 'd']);
    print(reject(['a', 'b', 3, 'd'], lambda x: type(x) == str), [3]);