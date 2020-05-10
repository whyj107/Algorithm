# 문제
# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.

# 입력 == 출력
# test.assert_equals(summation(1), 1)
# test.assert_equals(summation(8), 36)
# test.assert_equals(summation(22), 253)
# test.assert_equals(summation(100), 5050)
# test.assert_equals(summation(213), 22791)

# My Code
def summation(num):
    return (num + 1) * num // 2
    return sum(xrange(num + 1))

if __name__=='__main__':
    print(summation(1))
    print(summation(8))
    print(summation(22))
    print(summation(100))
    print(summation(213))