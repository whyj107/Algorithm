# 문제
# Twisted Sum
# https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f/train/python

# 나의 풀이
def compute_sum(n):
    return sum(list(map(int, ''.join(list(map(str, range(1, n+1)))))))

# 다른 사람의 풀이
def compute_sum1(n):
    return sum(int(c) for i in range(1, n+1) for c in str(i))


if __name__ == '__main__':
    print(compute_sum(1), 1)
    print(compute_sum(2), 3)
    print(compute_sum(3), 6)
    print(compute_sum(4), 10)
    print(compute_sum(10), 46)
    print(compute_sum(12), 51)
