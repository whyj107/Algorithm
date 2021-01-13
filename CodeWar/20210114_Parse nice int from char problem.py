# Parse nice int from char problem
# https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1/train/python

# 나의 풀이
def get_age(age):
    return int(age.split(' ')[0])

# 다른 사람의 문제 풀이
def get_age1(age):
    return int(age[0])

print(get_age("2 years old"), 2)
print(get_age("4 years old"), 4)
print(get_age("5 years old"), 5)
print(get_age("7 years old"), 7)