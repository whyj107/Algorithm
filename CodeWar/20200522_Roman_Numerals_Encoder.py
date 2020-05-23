# 문제
# Roman Numerals Encoder
# Create a function taking a positive integer as its parameter
# and returning a string containing the Roman Numeral representation of that integer.
#
# Modern Roman numerals are written by expressing each digit separately starting
# with the left most digit and skipping any digit with a value of zero.
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII.
# 1666 uses each Roman symbol in descending order: MDCLXVI.

# 입력 == 출력
# test.assert_equals(solution(1),'I', "solution(1),'I'")
# test.assert_equals(solution(4),'IV', "solution(4),'IV'")
# test.assert_equals(solution(6),'VI', "solution(6),'VI'")
# test.assert_equals(solution(14),'XIV', "solution(14),'XIV")
# test.assert_equals(solution(21),'XXI', "solution(21),'XXI'")
# test.assert_equals(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
# test.assert_equals(solution(91),'XCI', "solution(91),'XCI'")
# test.assert_equals(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
# test.assert_equals(solution(1000), 'M', 'solution(1000), M')
# test.assert_equals(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
# test.assert_equals(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")

# My Code
def solution0(n):
    roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    answer = ''
    if n in roman:
        return roman[n]
    while n != 0:
        if n >= 1000:
            answer += roman[1000]
            n -= 1000
        elif n >= 900:
            answer += (roman[100] + roman[1000])
            n -= 900
        elif n >= 500:
            answer += roman[500]
            n -= 500
        elif n >= 400:
            answer += (roman[100] + roman[500])
            n -= 400
        elif n >= 100:
            answer += roman[100]
            n -= 100
        elif n >= 90:
            answer += (roman[10] + roman[100])
            n -= 90
        elif n >= 50:
            answer += roman[50]
            n -= 50
        elif n >= 40:
            answer += (roman[10] + roman[50])
            n -= 40
        elif n >= 10:
            answer += roman[10]
            n -= 10
        elif n >= 9:
            answer += (roman[1] + roman[10])
            n -= 9
        elif n >= 5:
            answer += roman[5]
            n -= 5
        elif n == 4:
            answer += (roman[1] + roman[5])
            n -= 4
        else:
            answer += roman[1]
            n -= 1
    return answer

# Warriors Code
vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))

def solution1(n):
    if n == 0: return ""
    return next(c + solution1(n-v) for c,v in vals if v <= n)

def solution(n):
    roman = {1: 'I', 4: 'IV', 5: 'V', 9:'IX',
             10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
             100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
             1000: 'M'}
    answer = ""
    for i in reversed(sorted((roman.keys()))):
        while i <= n:
            n -= i
            answer += roman[i]
    return answer


if __name__ == '__main__':
    print(solution(1000))
    print(solution(6))