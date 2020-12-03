# Sum - Square Even, Root Odd
# https://www.codewars.com/kata/5a4b16435f08299c7000274f/train/python

# 나의 풀이
def sum_square_even_root_odd(nums):
    return round(sum(i**2 if i%2 == 0 else i**0.5 for i in nums), 2)

# 다른 사람의 풀이
def sum_square_even_root_odd1(nums):
    return round(sum(n**(0.5 if n % 2 else 2) for n in nums), 2)

sum_square_even_root_odd2=lambda l:round(sum(x**[2,.5][x&1]for x in l),2)

print(sum_square_even_root_odd([4, 5, 7, 8, 1, 2, 3, 0]), 91.61)
print(sum_square_even_root_odd([1, 14, 9, 8, 17, 21]), 272.71)
