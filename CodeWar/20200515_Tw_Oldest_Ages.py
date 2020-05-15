# 문제
# Two Oldest Ages
# The two oldest ages function/method needs to be completed.
# It should take an array of numbers as its argument
# and return the two highest numbers within the array.
# The returned value should be an array in the format [second oldest age, oldest age].
#
# The order of the numbers passed in could be any order.
# The array will always include at least 2 items.

# 입력 == 출력
# Test.assert_equals(two_oldest_ages([1, 5, 87, 45, 8, 8]), [45, 87])
# Test.assert_equals(two_oldest_ages([6, 5, 83, 5, 3, 18]), [18, 83])
# Test.assert_equals(two_oldest_ages([10, 1]), [1, 10])

# My Code
def two_oldest_ages(ages):
    ages.sort()
    return [ages[-2], ages[-1]]

def two_oldest_ages1(ages):
    return sorted(ages)[-2:]

if __name__ == '__main__':
    print(two_oldest_ages([1, 5, 87, 45, 8, 8]))
    print(two_oldest_ages([6, 5, 83, 5, 3, 18]))
    print(two_oldest_ages([10, 1]))