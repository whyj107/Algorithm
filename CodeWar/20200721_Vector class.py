# 문제
# Vector class

# 나의 풀이
class Vector:
    def __init__(self, v):
        self.v = v
        self.len = len(v)

    def __str__(self):
        return '(' + ','.join(map(str, self.v)) + ')'

    def add(self, v2):
        if self.len == len(v2.v):
            return Vector([self.v[i] + v2.v[i] for i in range(self.len)])
        else:
            raise

    def subtract(self, v2):
        if self.len == len(v2.v):
            return Vector([self.v[i] - v2.v[i] for i in range(self.len)])
        else:
            raise

    def dot(self, v2):
        if self.len == len(v2.v):
            return sum([self.v[i] * v2.v[i] for i in range(self.len)])
        else:
            raise

    def norm(self):
        return sum([i ** 2 for i in self.v]) ** 0.5

    def equals(self, v2):
        if self.len == len(v2.v):
            for i in range(self.len):
                if self.v[i] != v2.v[i]:
                    return False
            return True

# 다른 사람의 풀이
from operator import add, sub, mul
from math import sqrt
class Vector1(object):
    def __init__(self, values):
        assert (isinstance(values, list))
        self.values = list(values)

    """ Combines elements pairwise w.r.t. given operator"""

    def __combine(self, other, operator):
        assert (isinstance(other, Vector))
        assert (len(self.values) == len(other.values))
        return map(operator, self.values, other.values)

    def add(self, other):
        return Vector(self.__combine(other, add))

    def subtract(self, other):
        return Vector(self.__combine(other, sub))

    def dot(self, other):
        return sum(self.__combine(other, mul))

    def norm(self):
        return sqrt(sum(i * i for i in self.values))

    def equals(self, other):
        return self.values == other.values

    def __str__(self):
        return '(' + str(self.values).replace(' ', '')[1:-1] + ')'

if __name__ == '__main__':
    a = Vector([1, 2])
    b = Vector([3, 4])
    print(a.add(b).equals(Vector([4, 6])))

    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])

    print(a.add(b).equals(Vector([4, 6, 8])))
    print(a.subtract(b).equals(Vector([-2, -2, -2])))
    print(a.dot(b), 26)
    print(a.norm(), 14 ** 0.5)