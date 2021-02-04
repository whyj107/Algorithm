# Letterbox Paint-Squad
# https://www.codewars.com/kata/597d75744f4190857a00008d/train/python

# 나의 풀이
def paint_letterboxes(start, finish):
    return [''.join(str(i) for i in range(start, finish+1, 1)).count(str(i)) for i in range(10)]

# 다른 사람의 풀이
from collections import Counter
def paint_letterboxes1(s, f):
    a = Counter("".join(map(str, range(s, f+1))))
    return [a[x] for x in "0123456789"]

print(paint_letterboxes(125, 132), [1, 9, 6, 3, 0, 1, 1, 1, 1, 1])