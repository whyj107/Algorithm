# Disarium Number (Special Numbers Series #3)
# https://www.codewars.com/kata/5a53a17bfd56cb9c14000003/train/python

# 나의 풀이
def disarium_number(number):
    return "Disarium !!" if sum(pow(int(n), i+1) for i, n in enumerate(str(number))) == number else "Not !!"

# 다른 사람의 풀이
def disarium_number1(n):
    return "Disarium !!" if n == sum(int(d)**i for i, d in enumerate(str(n), 1)) else "Not !!"

print(disarium_number(89)  , "Disarium !!")
print(disarium_number(518) , "Disarium !!")
print(disarium_number(1024), "Not !!")