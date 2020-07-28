# 문제
# Grouped by commas
# https://www.codewars.com/kata/5274e122fc75c0943d000148/train/python

# 나의 풀이
def group_by_commas(n):
    return ''.join([i+',' if idx%3 ==0 and idx != 0 else i for idx, i in enumerate(str(n)[::-1])][::-1])

# 다른 사람의 풀이
def group_by_commas1(n):
    return '{:,}'.format(n)

if __name__ == '__main__':
    print(group_by_commas(1), '1')
    print(group_by_commas(10), '10')
    print(group_by_commas(100), '100')
    print(group_by_commas(1000), '1,000')
    print(group_by_commas(10000), '10,000')
    print(group_by_commas(100000), '100,000')
    print(group_by_commas(1000000), '1,000,000')
    print(group_by_commas1(35235235), '35,235,235')