# 문제
# Square(n) Sum
# Complete the square sum function so that it squares each number passed into it
# and then sums the results together.
#
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

# 입력 == 출력
# Test.assert_equals(square_sum([1,2]), 5)
# Test.assert_equals(square_sum([0, 3, 4, 5]), 50)

# My Code
def square_sum(numbers):
    return sum([i * i for i in numbers])
    return sum(i ** 2 for i in numbers)

if __name__=='__main__':
    print(square_sum([1, 2]))
    print(square_sum([0, 3, 4, 5]))