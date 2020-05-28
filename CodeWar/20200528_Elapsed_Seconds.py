# 문제
# Elapsed Seconds
# Complete the function so that it returns the number of seconds
# that have elapsed between the start and end times given.

# 입력 == 출력
# from datetime import datetime
#
# Test.describe("Basic tests")
# start = datetime(2013, 1, 1, 0, 0, 1)
# end = datetime(2013, 1, 1, 0, 0, 2)
# end2 = datetime(2013, 1, 1, 0, 0, 20)
# end3 = datetime(2013, 1, 1, 0, 1, 20)
#
# Test.assert_equals(elapsed_seconds(start, end), 1)
# Test.assert_equals(elapsed_seconds(end, end2), 18)
# Test.assert_equals(elapsed_seconds(start, end2), 19)
# Test.assert_equals(elapsed_seconds(start, end3), 79)
# Test.assert_equals(elapsed_seconds(end, end3), 78)

# My Code
def elapsed_seconds(start, end):
    return (end - start).seconds

# Warriors Code
def elapsed_seconds1(start, end):
    return (end - start).total_seconds()

if __name__ == '__main__':
    from datetime import datetime

    start = datetime(2013, 1, 1, 0, 0, 1)
    end = datetime(2013, 1, 1, 0, 0, 2)
    end2 = datetime(2013, 1, 1, 0, 0, 20)
    end3 = datetime(2013, 1, 1, 0, 1, 20)

    print(elapsed_seconds1(start, end), 1)
    print(elapsed_seconds(end, end2), 18)
    print(elapsed_seconds(start, end2), 19)
    print(elapsed_seconds(start, end3), 79)
    print(elapsed_seconds(end, end3), 78)