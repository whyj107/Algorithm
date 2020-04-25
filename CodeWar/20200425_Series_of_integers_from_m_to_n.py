# 문제
# Task
# Write a function that accepts two arguments and
# generates a sequence containing the integers from the first argument to the second inclusive.
#
# Input
# Pair of integers greater than or equal to 0.
# The second argument will always be greater than or equal to the first.

# 입력 == 출력
# test.assert_equals(generate_integers(2, 5), [2, 3, 4, 5])

# My Code
def generate_integers(m, n):
    return [i for i in range(m, n + 1)]
    # return list(range(m, n + 1))

if __name__=='__main__':
    print(generate_integers(2, 5))