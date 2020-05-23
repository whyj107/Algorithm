# 문제
# Pyramid Array
# Write a function that when given a number >= 0,
# returns an Array of ascending length subarrays.

# 입력 == 출력
# Test.assert_equals(pyramid(0), [])
# Test.assert_equals(pyramid(1), [[1]])
# Test.assert_equals(pyramid(2), [[1], [1, 1]])
# Test.assert_equals(pyramid(3), [[1], [1, 1], [1, 1, 1]])

# My Code
def pyramid(n):
    return [[1] * i for i in range(1, n+1)]

if __name__ == '__main__':
    print(pyramid(0), [])
    print(pyramid(1), [[1]])
    print(pyramid(2), [[1], [1, 1]])
    print(pyramid(3), [[1], [1, 1], [1, 1, 1]])