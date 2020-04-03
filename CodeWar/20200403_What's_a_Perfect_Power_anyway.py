# 문제
# A perfect power is a classification of positive integers:
# In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer.
# More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.
#
# Your task is to check wheter a given integer is a perfect power. If it is a perfect power,
# return a pair m and k with mk = n as a proof. Otherwise return Nothing,
# Nil, null, NULL, None or your language's equivalent.
#
# Note: For a perfect power, there might be several pairs.
# For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions.
# However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.

# 입력 == 출력
# Test.assert_equals(isPP(4), [2,2], "4 = 2^2")
# Test.assert_equals(isPP(9), [3,2], "9 = 3^2")
# Test.assert_equals(isPP(5), None, "5 isn't a perfect power")

# My Code
import math
# 에라토스테네스 체 이용 - 소수가 아닌 수는 결국 깔끔하게 짝이 안지어질 확률이 높으니까
def isPP(n):
    # 효율적으로 코딩하기 위해서는 n의 제곱근까지만 확인
    for m in range(2, int(math.sqrt(n)) + 1):
        # 지수함수의 역연산이 필요하므로 log 사용
        # ex) log3 81 = 4
        k = int(math.log(n, m))
        # 정확하게 맞아 떨어지면 값 return(없을 경우 None이 return)
        if m ** k == n:
            return [m, k]
    return None

# Warriors Code
def isPP_(n):
    for i in range(2, int(n**.5) + 1):
        number = n
        times = 0
        while number % i == 0:
            number /= i
            times += 1
            if number == 1:
                return [i, times]
    return None

if __name__=='__main__':
    answer = isPP(4)
    print(answer)
    answer = isPP(9)
    print(answer)
    answer = isPP(5)
    print(answer)