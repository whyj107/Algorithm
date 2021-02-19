# Divide and Conquer
# https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python

# 나의 풀이
def div_con(x):
    return sum(i if type(i) is int else -1 * int(i) for i in x)

# 다른 사람의 풀이
def div_con1(lst):
    return sum(n if isinstance(n, int) else -int(n) for n in lst)

print(div_con([9, 3, '7', '3']), 2)
print(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 14)
print(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 13)
print(div_con(['1', '5', '8', 8, 9, 9, 2, '3']), 11)
print(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)
