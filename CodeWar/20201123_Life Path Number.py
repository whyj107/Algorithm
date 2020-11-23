# Life Path Number
# https://www.codewars.com/kata/5a1a76c8a7ad6aa26a0007a0/train/python

# 나의 풀이
def solve(num):
    while len(num) > 1:
        num = str(sum(int(i) for i in num))
    return int(num)

def life_path_number(birthdate):
    year, month, day = map(str, birthdate.split('-'))
    return solve(str(solve(year) + solve(month) + solve(day)))

# 다른 사람의 풀이
def life_path_number1(s):
    return int(s.replace("-", "")) % 9 or 9

def sumDigits(n):
    s = sum([int(n) for n in str(n)])
    if s >= 10:
        return sumDigits(s)
    return s

def life_path_number2(birthdate):
    return sumDigits(sum([sumDigits(n) for n in birthdate.split("-")]))

def life_path_number3(birthdate):
    n = "".join(i for i in birthdate if i.isdigit())
    while len(str(n)) > 1:
        n = sum(i for i in map(int, str(n)))
    return n


print(life_path_number("1955-10-28"), 4)
print(life_path_number("1971-06-28"), 7)
