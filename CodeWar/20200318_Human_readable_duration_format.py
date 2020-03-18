# 문제
# Your task in order to complete this Kata is to write a function which formats a duration,
# given as a number of seconds, in a human-friendly way.
# The function must accept a non-negative integer.
# If it is zero, it just returns "now".
# Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# Note that spaces are important.
# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc.
# In general, a positive integer and one of the valid units of time,separated by a space.
# The unit of time is used in plural if the integer is greater than 1.

# The components are separated by a comma and a space (", ").
# Except the last component, which is separated by " and ",
# just like it would be written in English.
# A more significant units of time will occur before than a least significant one.
# Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
# Different components have different unit of times.
# So there is not repeated units like in 5 seconds and 1 second.
# A component will not appear at all if its value happens to be zero.
# Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
# A unit of time must be used "as much as possible".
# It means that the function should not return 61 seconds,
# but 1 minute and 1 second instead.
# Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

# 입력 == 출력
# test.assert_equals(format_duration(1), "1 second")
# test.assert_equals(format_duration(62), "1 minute and 2 seconds")
# test.assert_equals(format_duration(120), "2 minutes")
# test.assert_equals(format_duration(3600), "1 hour")
# test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")

# --------------------------
# 문제가 이해하기 어렵네?
#
# --------------------------
import time
from datetime import datetime, timedelta

# My Code
def format_duration(seconds):
    answer = timedelta(seconds=seconds)
    print(answer)
    return answer

if __name__=='__main__':
    answer = format_duration(1)
    print(answer)
    answer = format_duration(62)
    print(answer)
    answer = format_duration(3662)
    print(answer)
    answer = format_duration(86400*365)
    print(answer)