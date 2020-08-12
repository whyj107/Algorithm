# 문제
# Normalizing Out of Range Array Indexes
# https://www.codewars.com/kata/5285bf61f8fc1b181700024c/train/python

# 나의 풀이
def norm_index_test(seq, ind):
    return seq[ind%len(seq)] if seq != [] else None

# 다른 사람의 풀이
def norm_index_test1(a, n):
    if a: return a[n % len(a)]

if __name__ == '__main__':
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(norm_index_test(seq, 0), 0)
    print(norm_index_test(seq, 1), 1)
    print(norm_index_test(seq, -1), 9)
    print(norm_index_test(seq, 10), 0)
    print(norm_index_test([], 10), None)