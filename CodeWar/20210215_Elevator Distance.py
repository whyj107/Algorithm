# Elevator Distance
# https://www.codewars.com/kata/59f061773e532d0c87000d16/train/python

# 나의 풀이
def elevator_distance(array):
    return sum(abs(array[i-1] - array[i]) for i in range(1, len(array)))

# 다른 사람의 풀이
def elevator_distance1(array):
    return sum(abs(a - b) for a, b in zip(array, array[1:]))

print(elevator_distance([5, 2, 8]), 9)
print(elevator_distance([1, 2, 3]), 2)
print(elevator_distance([7, 1, 7, 1]), 18)