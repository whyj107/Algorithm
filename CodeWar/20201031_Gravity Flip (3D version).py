# Gravity Flip (3D version)
# https://www.codewars.com/kata/5f849ab530b05d00145b9495/train/python

# 나의 풀이
def flip0(d, a):
    if d is 'R':
        return [sorted(i) for i in a]
    elif d is 'L':
        return [sorted(i, reverse=True) for i in a]
    tmp = []
    if d is 'U':
        for i in zip(*a):
            tmp.append(sorted(i, reverse=True))
    elif d is 'D':
        for i in zip(*a):
            tmp.append(sorted(i))
    return [list(i) for i in zip(*tmp)]

def flip(d, a):
    if d is 'R':
        return [sorted(i) for i in a]
    elif d is 'L':
        return [sorted(i, reverse=True) for i in a]
    elif d is 'U':
        return [list(i) for i in zip(*[sorted(i, reverse=True) for i in zip(*a)])]
    elif d is 'D':
        return [list(i) for i in zip(*[sorted(i) for i in zip(*a)])]

# 다른 사람의 풀이
rotate = lambda d,m: list(list(r) for r in zip(*m))

flip1   = lambda d,m: [sorted(r, reverse=d=='L') for r in m] if d in 'LR' else \
                     rotate(d, map(lambda r: sorted(r, reverse=d=='U'), rotate(d, m)))


box = [[1, 3, 2],
       [4, 5, 1],
       [6, 5, 3],
       [7, 2, 9]]

print(flip('R', box) == [[1, 2, 3],
                        [1, 4, 5],
                        [3, 5, 6],
                        [2, 7, 9]])

print(flip('L', box) == [[3, 2, 1],
                        [5, 4, 1],
                        [6, 5, 3],
                        [9, 7, 2]])

print(flip('U', box) == [[7, 5, 9],
                        [6, 5, 3],
                        [4, 3, 2],
                        [1, 2, 1]])

print(flip('D', box) == [[1, 2, 1],
                        [4, 3, 2],
                        [6, 5, 3],
                        [7, 5, 9]])
