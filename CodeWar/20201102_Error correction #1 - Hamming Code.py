# Error correction #1 - Hamming Code
# https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e/train/python

# 나의 풀이
# encode
# 모든 글자 아스키 값으로 변경
# 아스키 값을 8비트 binary string으로 변경
# 0을 000으로 변경, 1을 111로 변경

# decode
# 3개씩 끊는다.
# 000은 0으로 111은 1로 바꾼다
# 000이나 111이 아닌 것은 3개중에 많은 갯수의 수로 바꾼다.
# 이것들을 아스키 값을 이용하여 문자열로 바꾼다.

def encode0(string):
    step_one_two = ["{0:b}".format(ord(s)) for s in string]
    step_two = ''.join(["0"*(8-len(i))+i for i in step_one_two])
    step_three = step_two.replace("0", "000").replace("1", "111")
    return step_three

def encode(string):
    step_one_two = ''.join(["{0:b}".format(ord(s)).zfill(8) for s in string])
    step_three = step_one_two.replace("0", "000").replace("1", "111")
    return step_three

def decode(bits):
    step_one = list(map(''.join, zip(*[iter(bits)]*3)))
    step_two = list(map(''.join, zip(*[iter(["0" if i.count("1") < i.count("0") else "1" for i in step_one])]*8)))
    step_three = [chr(int(i, 2)) for i in step_two]
    return ''.join(step_three)

print(encode("hey") ==  '000111111000111000000000000111111000000111000111000111111111111000000111')
print(decode("100111111000111001000010000111111000000111001111000111110110111000010111"), "hey")