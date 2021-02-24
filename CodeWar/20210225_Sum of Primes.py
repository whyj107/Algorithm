# Sum of Primes
# https://www.codewars.com/kata/5902ea9b378a92a990000016/train/python

# 나의 풀이
def isprime(n):
    if n < 2: return False
    for i in range(2, round(n**0.5)+1):
        if n % i == 0: return False
    return True

def sum_primes(lower, upper):
    return sum(i for i in range(lower, upper+1) if isprime(i))

# 다른 사람의 풀이
from gmpy2 import next_prime

def sum_primes1(l, u):
    s = 0
    c = next_prime(l-1)
    while c<=u:
        s+=c
        c = next_prime(c)
    return s

print(sum_primes(4, 20), 72)
print(sum_primes(20, 4), 0)
print(sum_primes(2, 7), 17)
print(sum_primes(1, 30), 129)