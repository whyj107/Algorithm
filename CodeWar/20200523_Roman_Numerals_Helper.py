# 문제
# Roman Numerals Helper
# Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered:
# 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII.
# 1666 uses each Roman symbol in descending order: MDCLXVI.

# 입력 == 출력
# test.assert_equals(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
# test.assert_equals(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
#
# test.assert_equals(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
# test.assert_equals(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')

# My Code
class RomanNumerals:
    def to_roman( n):
        roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        answer = ""
        for i in reversed(sorted((roman.keys()))):
            while i <= n:
                n -= i
                answer += roman[i]
        return answer

    def from_roman(roman):
        n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        answer = 0
        for i in range(0, len(roman) - 1):
            if n[roman[i]] >= n[roman[i + 1]]:
                answer += n[roman[i]]
            else:
                answer -= n[roman[i]]
        return answer + n[roman[-1]]

if __name__ == '__main__':
    print(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
    print(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
    print(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
    print(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')
