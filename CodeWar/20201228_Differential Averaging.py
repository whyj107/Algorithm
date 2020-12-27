# Differential Averaging
# https://www.codewars.com/kata/52c32ef251f31ae8f50000ae/train/python

# 나의 풀이
def add_to_average(current, points, add):
    return (current * points + add) / (points+1)

# 다른 사람의 풀이
add_to_average1 = lambda current, points, add: (current*points + add)/(points+1)

print(add_to_average(0, 0, 1) == 1, "average of [1]")
print(add_to_average(1, 1, 2) == 1.5, "average of [1, 2]")
print(add_to_average(1.5, 2, 3) == 2, "average of [1, 2, 3]")
print(add_to_average(0, 0, 123) == 123, "average of [123]")
print(add_to_average(123, 1, 456) == 289.5, "average [123, 456]")
print(add_to_average(289.5, 2, 789) == 456, "average [123, 456, 789]")