# 문제
# No oddities here
# Write a small function that returns the values of an array that are not odd.
#
# All values in the array will be integers.
# Return the good values in the order they are given.

# 입력 == 출력
# Test.assert_equals(no_odds([0, 1]), [0], 'Zero through one')
# Test.assert_equals(no_odds([0, 1, 2, 3]), [0, 2], 'Zero through three')
# Test.assert_equals(no_odds([1, 3, 5, 7, 9]), [], 'Odds through ten')
# Test.assert_equals(no_odds([0, 2, 4, 6, 8, 10]), [0, 2, 4, 6, 8, 10], 'Evens through ten')
# Test.assert_equals(no_odds([-1, -3, -5, -7, -9]), [], 'Negative odds')
# Test.assert_equals(no_odds([2, 4, 8, 6, 0]), [2, 4, 8, 6, 0], 'Out of order')
# Test.assert_equals(no_odds([]), [], 'Empty list')

# My Code
def no_odds(values):
    return [i for i in values if i%2 == 0]

if __name__ == '__main__':
    print(no_odds([0, 1]), [0], 'Zero through one')
    print(no_odds([0, 1, 2, 3]), [0, 2], 'Zero through three')
    print(no_odds([1, 3, 5, 7, 9]), [], 'Odds through ten')
    print(no_odds([0, 2, 4, 6, 8, 10]), [0, 2, 4, 6, 8, 10], 'Evens through ten')
    print(no_odds([-1, -3, -5, -7, -9]), [], 'Negative odds')
    print(no_odds([2, 4, 8, 6, 0]), [2, 4, 8, 6, 0], 'Out of order')
    print(no_odds([]), [], 'Empty list')