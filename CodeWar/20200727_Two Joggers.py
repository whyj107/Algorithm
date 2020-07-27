# 문제
# Two Joggers
# https://www.codewars.com/kata/5274d9d3ebc3030802000165/train/python

# 나의 풀이
def nbr_of_laps(x, y):
    g = gcd(x, y)
    return (x*y//(g*x), x*y//(g*y))

def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

# 다른 사람의 풀이
from fractions import gcd

def nbr_of_laps(x, y):
    return (y / gcd(x,y), x / gcd(x,y))

if __name__ == '__main__':
    print(nbr_of_laps(5, 3), (3, 5))
    print(nbr_of_laps(4, 6), (3, 2))
    print(nbr_of_laps(5, 5), (1, 1))