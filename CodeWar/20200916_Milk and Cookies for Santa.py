# 문제
# Milk and Cookies for Santa
# https://www.codewars.com/kata/52af7bf41f5a1291a6000025/train/python

# 나의 풀이
def time_for_milk_and_cookies(dt):
    return (dt.month, dt.day) == (12, 24)

# 다른 사람의 풀이
def time_for_milk_and_cookies(dt):
    return dt.month * dt.day == 288

from datetime import date
print(time_for_milk_and_cookies(date(2013, 12, 24)), True)
print(time_for_milk_and_cookies(date(2013, 10, 24)), False)
print(time_for_milk_and_cookies(date(3000, 12, 24)), True)