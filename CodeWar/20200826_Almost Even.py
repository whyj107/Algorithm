# 문제
# Almost Even
# https://www.codewars.com/kata/529e2e1f16cb0fcccb000a6b/train/python

# 나의 풀이
def split_integer(num, parts):
    return [num//parts]*parts if num%parts == 0 else [num//parts]*(parts-num%parts)+[num//parts+1]*(num%parts)

# 다른 사람의 풀이
def splitInteger1(n, pp):
    p, bb = divmod(n, pp)
    return (pp - bb) * [p] + bb * [p + 1]

if __name__ == '__main__':
    print(split_integer(10, 1) == [10])
    print(split_integer(2, 2) == [1, 1])
    print(split_integer(20, 5) == [4, 4, 4, 4, 4])
    print(split_integer(20, 6), [3, 3, 3, 3, 4, 4])
    print(split_integer(20, 7), [2, 3, 3, 3, 3, 3, 3])