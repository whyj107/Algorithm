# Status Arrays
# https://www.codewars.com/kata/601c18c1d92283000ec86f2b/train/python

# 나의 풀이 : 문제가 이해되지 않아서 다른 사람의 풀이를 보고 이해했다.
def status1(nums):
    # a에 일단 한번 정렬
    a = sorted(nums)
    # tmp에 숫자와 인덱스 번호 쌍으로 묶음
    tmp = [(n, i) for i, n in enumerate(nums)]
    # 인덱스 + 정렬된 a에서의 인덱스값 더해서 정렬
    return [x[0] for x in sorted(tmp, key=lambda x: x[1] + a.index(x[0]))]

def status(nums):
    return [x[0] for x in sorted([(n, i) for i, n in enumerate(nums)], key=lambda x: x[1] + sorted(nums).index(x[0]))]

print(status([6, 9, 3, 8, 2, 3, 1]), [6, 3, 2, 1, 9, 3, 8])
print(status([5, 5, 5, 8, 7, -2, -2, -3, 1, 9, 8, 3, -3, 4, -4, 6]),
      [5, -2, -3, 5, -2, 5, 1, -3, -4, 8, 7, 3, 4, 8, 9, 6])
print(status([14, -3, 4, 6, 9, 10, -2, 4, 0]), [-3, 4, -2, 14, 6, 9, 4, 0, 10])