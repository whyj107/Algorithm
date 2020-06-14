# 문제
# Fibonacci Reloaded
# And here is Fibonacci again. This time we want to go one step further.
# Our fib() function must be faster! Can you do it?
#
# In case you don't know, what the Fibonacci number is:
#
# The nth Fibonacci number is defined by the sum of the two previous Fibonacci numbers.
# In our case: fib(1) == 0 and fib(2) == 1.
# With these initial values you should be able to calculate each following Fibonacci number.

# 입력 == 출력
# Test.assert_equals(fib(1), 0, 'fib(1) failed')
# Test.assert_equals(fib(2), 1, 'fib(2) failed')
# Test.assert_equals(fib(3), 1, 'fib(3) failed')
# Test.assert_equals(fib(4), 2, 'fib(4) failed')
# Test.assert_equals(fib(5), 3, 'fib(5) failed')

# My Code
def fib(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 2] + fib[i - 1]
    return fib[n - 1]

# Warriors Code
def fib1(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    print(fib(1), 0, 'fib(1) failed')
    print(fib(2), 1, 'fib(2) failed')
    print(fib(3), 1, 'fib(3) failed')
    print(fib(4), 2, 'fib(4) failed')
    print(fib(5), 3, 'fib(5) failed')