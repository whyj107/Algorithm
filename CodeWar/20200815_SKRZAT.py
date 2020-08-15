# 문제
# SKRZAT
# https://www.codewars.com/kata/528a0762f51e7a4f1800072a/train/python

# 나의 풀이
# 10923일경우 틀리게 나온다... 왜지?
def skrzat(base, number):
    if base == 'b':
        answer = 0
        for idx, i in enumerate(number[::-1]):
            answer += (int(i) * pow(-2, idx))
        return f'From binary: {number} is {answer}'
    elif base == 'd':
        b = int(number)
        answer = ''
        while b:
            answer += str(abs(b % 2))
            b = (b - b % 2)//-2
        return f'From decimal: {number} is {answer[::-1]}'

# 다른 사람의 풀이
def skrzat1(base, number):
    s = 0xAAAAAAAA
    if base == 'b':
        i = int(number, 2)
        return f"From binary: {number} is {(s ^ i) - s}"
    elif base == 'd':
        return f"From decimal: {number} is {(number + s) ^ s:b}"

if __name__ == '__main__':
    print(skrzat('b', '1001101') == 'From binary: 1001101 is 61')
    print(skrzat('b', '0111111') == 'From binary: 0111111 is -21')
    print(skrzat('d', -137) =='From decimal: -137 is 10001011')
    print(skrzat('d', 137) == 'From decimal: 137 is 110011001')
    print(skrzat('d', 10923))
    print(skrzat1('d', 10923))
    print(skrzat('d', 10924))
    print(skrzat1('d', 10924))