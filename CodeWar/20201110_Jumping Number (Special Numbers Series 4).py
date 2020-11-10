# Jumping Number (Special Numbers Series #4)
# https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/python

# 나의 풀이
def jumping_number(number):
    n = str(number)
    for i in range(1, len(n)):
        if abs(int(n[i-1])-int(n[i])) != 1:
            return "Not!!"
    return "Jumping!!"

# 다른 사람의 풀이
def jumping_number1(number):
    arr = list(map(int, str(number)))
    return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]

print(jumping_number(1), "Jumping!!")
print(jumping_number(7), "Jumping!!")
print(jumping_number(9), "Jumping!!")

print(jumping_number(23), "Jumping!!")
print(jumping_number(32), "Jumping!!")
print(jumping_number(79), "Not!!")
print(jumping_number(98), "Jumping!!")

print(jumping_number(8987), "Jumping!!")
print(jumping_number(4343456) , "Jumping!!")
print(jumping_number(98789876), "Jumping!!")
