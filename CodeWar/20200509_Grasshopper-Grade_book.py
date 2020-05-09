# 문제
# Complete the function so that it finds the mean of the three scores passed to it
# and returns the letter value associated with that grade.
# 90 <= score <= 100    : 'A'
# 80 <= score < 90      : 'B'
# 70 <= score < 80      : 'C'
# 60 <= score < 70      : 'D'
# 0 <= score < 60       : 'F'
# Tested values are all between 0 and 100.
# Theres is no need to check for negative values or values greater than 100.

# 입력 == 출력
# test.assert_equals(get_grade(95, 90, 93), "A", "get_grade(95, 90, 93)")
# test.assert_equals(get_grade(70, 70, 100), "B", "get_grade(70, 70, 100)")
# test.assert_equals(get_grade(70, 70, 70), "C", "get_grade(70, 70, 70)")
# test.assert_equals(get_grade(65, 70, 59), "D", "get_grade(65, 70, 59)")
# test.assert_equals(get_grade(44, 55, 52), "F", "get_grade(44, 55, 52)")

# My Code
def get_grade(s1, s2, s3):
    avg_ = (s1 + s2 + s3)//3

    if avg_ >= 90:
        return 'A'
    elif avg_ >= 80:
        return 'B'
    elif avg_ >= 70:
        return 'C'
    elif avg_ >= 60:
        return 'D'
    else:
        return 'F'

    return 'A' if avg_ >= 90 else ('B' if avg_ >= 80 else ('C' if avg_ >= 70 else ('D' if avg_ >= 60 else 'F')))

    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')

if __name__=='__main__':
    print(get_grade(95, 90, 93))
    print(get_grade(70, 70, 100))
    print(get_grade(70, 70, 70))
    print(get_grade(65, 70, 59))
    print(get_grade(44, 55, 52))