# 문제
# Human Readable Time
# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# 입력 == 출력
# Test.assert_equals(make_readable(0), "00:00:00")
# Test.assert_equals(make_readable(5), "00:00:05")
# Test.assert_equals(make_readable(60), "00:01:00")
# Test.assert_equals(make_readable(86399), "23:59:59")
# Test.assert_equals(make_readable(359999), "99:59:59")

# My Code
def make_readable(seconds):
    return '{0:02d}:{1:02d}:{2:02d}'.format((seconds%(60*60*100))//(60*60), (seconds%(60*60))//60, seconds%60)

# Warriors Code
def make_readable1(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

if __name__ == '__main__':
    print(make_readable(0), "00:00:00")
    print(make_readable(5), "00:00:05")
    print(make_readable(60), "00:01:00")
    print(make_readable(10800), "03:00:00")
    print(make_readable(86399), "23:59:59")
    print(make_readable(359999), "99:59:59")