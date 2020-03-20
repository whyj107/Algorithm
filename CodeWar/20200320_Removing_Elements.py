# 문제
# Take an array and remove every second element out of that array.
# Always keep the first element and start removing with the next element.

# Example:
# my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
# None of the arrays will be empty, so you don't have to worry about that!

# 입력 == 출력
# test.assert_equals(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
#                    ['Hello', 'Hello Again'])
# test.assert_equals(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
#                    [1, 3, 5, 7, 9])
# test.assert_equals(remove_every_other([[1, 2]]), [[1, 2]])
# test.assert_equals(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
#                    [['Goodbye']])

# --------------------------
# 짝수번째에 있는 항목 제거
# --------------------------

# My Code
def remove_every_other(my_list):
    answer = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            answer.append(my_list[i])
    return answer

# Warriors Code
def remove_every_other_(my_list):
    return my_list[::2]

if __name__=='__main__':
    r = remove_every_other(['Hello', 'Goodbye', 'Hello Again'])
    print(r)
    r = remove_every_other_([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(r)
    r = remove_every_other([[1, 2]])
    print(r)
    r = remove_every_other([['Goodbye'], {'Great': 'Job'}])
    print(r)