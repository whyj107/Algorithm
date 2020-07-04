# 문제
# Bit Counting
# Write a function that takes an integer as input,
# and returns the number of bits that are equal to one in the binary representation of that number.
# You can guarantee that input is non-negative.
#
# Example: The binary representation of 1234 is 10011010010,
# so the function should return 5 in this case

# 입력 == 출력
# test.assert_equals(countBits(0), 0);
# test.assert_equals(countBits(4), 1);
# test.assert_equals(countBits(7), 3);
# test.assert_equals(countBits(9), 2);
# test.assert_equals(countBits(10), 2);

# My Code
def countBits(n):
    return bin(n).count("1")

if __name__ == '__main__':
    print(countBits(0), 0);
    print(countBits(4), 1);
    print(countBits(7), 3);
    print(countBits(9), 2);
    print(countBits(10), 2);