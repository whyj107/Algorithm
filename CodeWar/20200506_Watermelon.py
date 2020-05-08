# 문제
# It's too hot, and they can't even…
# One hot summer day Pete and his friend Billy decided to buy watermelons.
# They chose the biggest crate.
# They rushed home, dying of thirst, and decided to divide their loot,
# however they faced a hard problem.
#
# Pete and Billy are great fans of even numbers,
# that's why they want to divide the number of watermelons in such a way
# that each of the two parts consists of an even number of watermelons.
# However, it is not obligatory that the parts are equal.
#
# Example: the boys can divide a stack of 8 watermelons into 2+6 melons, or 4+4 melons.
#
# The boys are extremely tired and want to start their meal as soon as possible,
# that's why you should help them and find out,
# whether they can divide the fruits in the way they want.
# For sure, each of them should get a part of positive weight.
#
# Task
# Given an integral number of watermelons w (1 ≤ w ≤ 100; 1 ≤ w in Haskell),
# check whether Pete and Billy can divide the melons so that each of them gets an even amount.

# 입력 == 출력
# test.assert_equals(divide(4), True)
# test.assert_equals(divide(2), False)
# test.assert_equals(divide(5), False)
# test.assert_equals(divide(88), True)
# test.assert_equals(divide(100), True)
# test.assert_equals(divide(67), False)
# test.assert_equals(divide(90), True)
# test.assert_equals(divide(10), True)
# test.assert_equals(divide(99), False)
# test.assert_equals(divide(32), True)

# My Code
def divide(weight):
    # weight가 3이하면 2개로 나누었을 때 짝수가 될 수 없다.
    if weight > 3:
        if weight % 2 == 0:
            return True
        else:
            return False
    else:
        return False
    # 한줄로 줄이면 다음과 같다.
    return (True if weight % 2 == 0 else False) if weight > 3 else False

if __name__=='__main__':
    print(divide(4))
    print(divide(2))
    print(divide(5))
    print(divide(88))
    print(divide(100))
    print(divide(67))
    print(divide(90))
    print(divide(10))
    print(divide(99))
    print(divide(32))