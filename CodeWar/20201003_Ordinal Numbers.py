# 문제
# Ordinal Numbers
# https://www.codewars.com/kata/52dda52d4a88b5708f000024/train/python

# 나의 풀이
def ordinal(number, brief=False):
    d = {1: "st", 2: "nd", 3: "rd"}
    if number%100 in [11, 12, 13]:
        return "th"
    if number % 10 in d:
        if brief and number%10 != 1:
            return "d"
        else:
            return d[number % 10]
    else:
        return "th"

# 다른 사람의 풀이
def ordinal1(n, brief=False):
    n %= 100
    if 9 < n < 20:
        return "th"
    n %= 10
    if n == 1:
        return "st"
    if n == 2:
        return "nd"[brief:]
    if n == 3:
        return "rd"[brief:]
    return "th"

print(ordinal(111))