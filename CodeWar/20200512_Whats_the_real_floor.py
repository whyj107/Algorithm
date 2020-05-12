# 문제
# What's the real floor?
# Europeans are odd people:
# in their buildings, the first floor is actually the ground floor
# and there is no 13th floor (due to superstition).
#
# Write a function that given an universal level (passed as an int) returns the European floor.
#
# With the 1st floor being replaced by the ground floor
# and the 13th floor being removed, the numbers move down to take their place.
# In case of above 13, they move down by two because there are two omitted numbers below them.
#
# Basements (negatives) stay the same as the universal level.

# 입력 == 출력
# test.assert_equals(get_real_floor(1), 0)
# test.assert_equals(get_real_floor(5), 4)
# test.assert_equals(get_real_floor(15), 13)

def get_real_floor(n):
    if n <= 0:
        return n
    elif n < 13:
        return n - 1
    else:
        return n - 2

    return n if n <= 0 else(n - 1 if n < 13 else n - 2)

if __name__=='__main__':
    print(get_real_floor(1))
    print(get_real_floor(0))
    print(get_real_floor(5))
    print(get_real_floor(15))
    print(get_real_floor(-3))

