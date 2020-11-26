# STRONGN Strong Number (Special Numbers Series #2)
# https://www.codewars.com/kata/5a4d303f880385399b000001/train/python

# 나의 풀이
def fact(n):
    return 1 if n == 0 else n*fact(n-1)
def strong_num(number):
    fac = sum([fact(int(n)) for idx, n in enumerate(str(number)[::-1])])
    return "STRONG!!!!" if number == fac else "Not Strong !!"

# 다른 사람의 풀이
import math
def strong_num1(number):
    return "STRONG!!!!" if sum(math.factorial(int(i)) for i in str(number)) == number else "Not Strong !!"


# 이 사람은 꼼수로 풀었다.
STRONGS = {1, 2, 145, 40585}
def strong_num2(number):
    return "STRONG!!!!" if number in STRONGS else "Not Strong !!"

print(strong_num(1)  , "STRONG!!!!")
print(strong_num(2)  , "STRONG!!!!")
print(strong_num(145), "STRONG!!!!")
print(strong_num(7)  , "Not Strong !!")
print(strong_num(93) , "Not Strong !!")
print(strong_num(185), "Not Strong !!")
