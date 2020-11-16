# ORing arrays
# https://www.codewars.com/kata/5ac5e9aa3853da25d9000102/train/python

"""
zip_longest(*iterables, fillvalue=None)
: 길이가 다른 두 배열의 zip 기능을 사용할 수  있는 함수
fillvalue 에 인자 값을 지정하여 zip() 한수를 적용해 준다.
"""
# 나의 풀이
from itertools import zip_longest
def or_arrays(arr1, arr2, n=0):
    return [i|j for i, j in zip_longest(arr1, arr2, fillvalue=n)]

# 풀이
def or_arrays0(arr1, arr2, n=0):
    result = []
    for i in range(max(len(arr1), len(arr2))):
        a = b = n
        if i < len(arr1): a = arr1[i]
        if i < len(arr2): b = arr2[i]
        result.append(b|a)
    return result

from itertools import zip_longest
def or_arrays1(a1, a2, d=0):
    return [x|y for x,y in zip_longest(a1, a2, fillvalue=d)]

print(or_arrays([1, 2, 3], [1, 2, 3]), [1, 2, 3])
print(or_arrays([1, 2, 3], [4, 5, 6]), [5, 7, 7])
print(or_arrays([1, 2, 3], [1, 2]), [1, 2, 3])
print(or_arrays([1, 2], [1, 2, 3]), [1, 2, 3])
print(or_arrays([1, 2, 3], [1, 2, 3], 3), [1, 2, 3])