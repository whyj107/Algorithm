# 문제
# Find within array
# We'll create a function that takes in two parameters:
# a sequence (length and types of items are irrelevant)
# a function (value, index) that will be called on members of the sequence and their index.
# The function will return either true or false.
# Your function will iterate through the members of the sequence in order until the provided function returns true;
# at which point your function will return that item's index.
#
# If the function given returns false for all members of the sequence,
# your function should return -1.

# 입력 == 출력
# test.assert_equals(find_in_array([], true_if_even) , -1)
# test.assert_equals(find_in_array([1,3,5,6,7], true_if_even) , 3)
# test.assert_equals(find_in_array([2,4,6,8], true_if_even) , 0)
# test.assert_equals(find_in_array([2,4,6,8], never_true) , -1)
# test.assert_equals(find_in_array([13,5,3,1,4,5], true_if_value_equals_index) , 4)
# test.assert_equals(find_in_array(["one","two","three","four","five","six"], true_if_length_equals_index) , 4)
# test.assert_equals(find_in_array(["bc","af","d","e"], true_if_length_equals_index) , -1)

# enumerate 함수
# 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가진다.
# 이 함수는 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
# 보통 enumerate 함수는 for문과 함께 자주 사용된다.

# My Code
def find_in_array(seq, predicate):
    for index, value in enumerate(seq):
        if predicate(value, index):
            return index
    return -1

if __name__ == '__main__':
    true_if_even = lambda v, i: v % 2 == 0
    never_true = lambda v, i: False
    true_if_value_equals_index = lambda v, i: v == i
    true_if_length_equals_index = lambda v, i: len(v) == i

    print(find_in_array([], true_if_even), -1)
    print(find_in_array([1, 3, 5, 6, 7], true_if_even), 3)
    print(find_in_array([2, 4, 6, 8], true_if_even), 0)
    print(find_in_array([2, 4, 6, 8], never_true), -1)
    print(find_in_array([13, 5, 3, 1, 4, 5], true_if_value_equals_index), 4)
    print(find_in_array(["one", "two", "three", "four", "five", "six"], true_if_length_equals_index), 4)
    print(find_in_array(["bc", "af", "d", "e"], true_if_length_equals_index), -1)