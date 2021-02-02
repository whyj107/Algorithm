# Char Code Calculation
# https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/python

# 나의 풀이
def calc0(x):
    n = [str(ord(i)) for i in x]
    total1 = sum(map(int, ''.join(n)))
    total2 = sum(map(int, ''.join(n).replace('7', '1')))
    return total1-total2

def calc(x):
    return ''.join(str(ord(i)) for i in x).count('7') * 6

# 다른 사람의 풀이
def calc1(s):
    total1 = ''.join(map(lambda c: str(ord(c)), s))
    total2 = total1.replace('7', '1')
    return sum(map(int, total1)) - sum(map(int, total2))

print(calc('ABC'), 6)
print(calc('abcdef'), 6)
print(calc('ifkhchlhfd'), 6)
print(calc('aaaaaddddr'), 30)
print(calc('jfmgklf8hglbe'), 6)
print(calc('jaam'), 12)
print(calc('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), 96)