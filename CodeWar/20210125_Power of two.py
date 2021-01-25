# Power of two
# https://www.codewars.com/kata/534d0a229345375d520006a0/train/python

# 나의 풀이
def power_of_two(x):
    return format(x, '#b').count('1') == 1

# 다른 사람의 풀이
def power_of_two1(x):
    return x != 0 and ((x & (x - 1)) == 0)

def power_of_two2(num):
    return bin(num).count('1') == 1

def power_of_two3(x):
    return x and (not(x&(x-1)))

print(power_of_two(0), False)
print(power_of_two(1), True)
print(power_of_two(2), True)
print(power_of_two(5), False)
print(power_of_two(6), False)
print(power_of_two(4096), True)
