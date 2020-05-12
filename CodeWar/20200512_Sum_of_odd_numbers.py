# 문제
# Sum of odd numbers
# Given the triangle of consecutive odd numbers:
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:
#
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8

# 입력 == 출력
# Test.assert_equals(row_sum_odd_numbers(1), 1)
# Test.assert_equals(row_sum_odd_numbers(2), 8)
# Test.assert_equals(row_sum_odd_numbers(13), 2197)
# Test.assert_equals(row_sum_odd_numbers(19), 6859)
# Test.assert_equals(row_sum_odd_numbers(41), 68921)

# My Code
def row_sum_odd_numbers(n):
    answer = []
    odd = 1
    for i in range(n):
        tmp = []
        for j in range(i + 1):
            tmp.append(odd)
            odd += 2
        answer.append(tmp)
    return sum(answer[n-1])

def row_sum_odd_number1(n):
    return n ** 3

if __name__=='__main__':
    print(row_sum_odd_numbers(1), 1)
    print(row_sum_odd_numbers(2), 8)
    print(row_sum_odd_numbers(13), 2197)
    print(row_sum_odd_numbers(19), 6859)
    print(row_sum_odd_number1(41), 68921)