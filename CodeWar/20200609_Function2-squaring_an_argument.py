# 문제
# Function 2 - squaring an argument
# Now you have to write a function
# that takes an argument and returns the square of it.

# 입력 == 출력
# test.assert_equals(square(2), 4)
# test.assert_equals(square(50), 2500)
# test.assert_equals(square(1), 1)

# My Code
def square(n):
    return n * n

if __name__ == '__main__':
    print(square(2), 4)
    print(square(50), 2500)
    print(square(1), 1)