# Get the mean of an array
# https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python

# 나의 풀이
def get_average(marks):
    return sum(marks)//len(marks)

# 다른 사람의 풀이
import numpy
def get_average1(marks):
    return int(numpy.mean(marks))

print(get_average([2, 2, 2, 2]), 2)
print(get_average([1, 5, 87, 45, 8, 8]), 25)
print(get_average([2, 5, 13, 20, 16, 16, 10]), 11)
print(get_average([1, 2, 15, 15, 17, 11, 12, 17, 17, 14, 13, 15, 6, 11, 8, 7]), 11)