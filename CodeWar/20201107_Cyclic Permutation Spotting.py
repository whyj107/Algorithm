# Cyclic Permutation Spotting
# https://www.codewars.com/kata/5f9d63c2ac08cb00338510f7/train/python

# 순환 순열인지 확인하는 문제
# (1, 2, 3)
# (2, 3, 1)
# 위와 같이 나오면 아래와 같다는 말
# 1 - 2 - 3 - 1
# 뭔 소린가 했네

# 나의 풀이
from typing import Tuple

def is_cyclic(p: Tuple[Tuple[int]]) -> bool:
    dic = {i: j for i, j in zip(*p)}
    tmp = p[0][0]
    try:
        while len(dic) != 0:
            tmp = dic.pop(tmp)
    except:
        return False
    return True

# 다른 사람의 풀이
def is_cyclic1(p):
    links = dict(zip(*p))
    m = next(iter(links))
    while m in links:
        m = links.pop(m)
    return not links

p = (
    (1, 2, 3, 4, 5, 6),
    (4, 3, 6, 2, 1, 5)
)
print(is_cyclic(p), True);

p = (
    (1, 2, 3, 4, 5, 6),
    (4, 6, 3, 2, 1, 5)
)
print(is_cyclic(p), False);

p = (
    (2, 8),
    (8, 2)
)
print(is_cyclic(p), True);

p = (
    (1, 2, 3, 4, 5, 6),
    (3, 1, 2, 5, 6, 4)
)
print(is_cyclic(p), False);


