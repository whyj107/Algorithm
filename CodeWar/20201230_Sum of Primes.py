# Sum of Primes
# https://www.codewars.com/kata/5902ea9b378a92a990000016/train/python

# 다른 사람의 풀이
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def sum_primes(lower, upper):
    return sum(i for i in range(lower, upper + 1) if is_prime(i))

print(sum_primes(4, 20), 72)
print(sum_primes(20, 4), 0)
print(sum_primes(2, 7), 17)
print(sum_primes(1, 30), 129)
print(sum_primes(60, 60), 0)