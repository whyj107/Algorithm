# 문제
# Is a number prime?
# Define a function that takes an integer argument
# and returns logical value true or false depending on if the integer is a prime.
#
# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1
# that has no positive divisors other than 1 and itself.

# 입력 == 출력
# Test.assert_equals(is_prime(0),  False, "0  is not prime")
# Test.assert_equals(is_prime(1),  False, "1  is not prime")
# Test.assert_equals(is_prime(2),  True, "2  is prime")
# Test.assert_equals(is_prime(73), True, "73 is prime")
# Test.assert_equals(is_prime(75), False, "75 is not prime")
# Test.assert_equals(is_prime(-1), False, "-1 is not prime")

# My Code
import math
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def is_prime1(num):
    if num < 2:
        return False

    for i in range(2, round(num**0.5)+1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(is_prime(0), False, "0  is not prime")
    print(is_prime(1), False, "1  is not prime")
    print(is_prime(2), True, "2  is prime")
    print(is_prime(73), True, "73 is prime")
    print(is_prime(75), False, "75 is not prime")
    print(is_prime(-1), False, "-1 is not prime")
