# 문제
# parseInt() reloaded
# In this kata we want to convert a string into an integer.
# The strings simply represent the numbers in words.
#
# Examples:
# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
# Additional Notes:
#
# The minimum number is "zero" (inclusively)
# The maximum number, which must be supported is 1 million (inclusively)
# The "and" in e.g. "one hundred and twenty-four" is optional,
# in some cases it's present and in others it's not
# All tested numbers are valid, you don't need to validate them

# 입력 == 출력
# Test.assert_equals(parse_int('one'), 1)
# Test.assert_equals(parse_int('twenty'), 20)
# Test.assert_equals(parse_int('two hundred forty-six'), 246)

# My Code
def parse_int(string):
    num = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
           "ten": 10, "eleven": 11, "twelve": 12, "thir": 3, "fif": 5, "eigh": 8,
           "teen": 10, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
           "hundred": 100, "thousand": 1000, "million": 1000000}
    answer = 0
    for i in string.split(" "):
        n = 0
        if i == "hundred" or i == "thousand" or i == "million":
            n = (answer % num[i]) * num[i]
            answer -= (answer % num[i])
        elif '-' in i:
            n = num[i.split('-')[0]] + num[i.split('-')[1]]
        elif 'teen' in i:
            n = num[i.replace('teen', '')] + 10
        elif 'and' == i:
            continue
        else:
            n = num[i]
        answer += n
    return answer

# Warriors Code
words = {w: n for n, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
words.update({w: 10 * n for n, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
thousands = {w: 1000 ** n for n, w in enumerate('thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion'.split(), 1)}
def parse_int1(strng):
    num = group = 0
    for w in strng.replace(' and ', ' ').replace('-', ' ').split():
        if w == 'hundred': group *= words[w]
        elif w in words: group += words[w]
        else:
            num += group * thousands[w]
            group = 0
    return num + group

if __name__ == '__main__':
    print(parse_int('six hundred sixty-six thousand six hundred sixty-six'), 666666)
    print(parse_int('six thousand three hundred and fifty-nine'), 6359)
    print(parse_int('one'), 1)
    print(parse_int('twenty'), 20)
    print(parse_int('two hundred forty-six'), 246)