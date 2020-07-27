# 문제
# Write out numbers
# https://www.codewars.com/kata/52724507b149fa120600031d/train/python

# 나의 풀이
num = {n: w for n, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
num.update({10 * n: w for n, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
def number2words(n):
    if n <= 20:
        return num[n]
    else:
        answer = []
        pre = 0
        for idx, nu in enumerate(str(n)[::-1]):
            tmp = idx % 3
            jari = 10 ** tmp

            if idx == 3:
                answer.append('thousand')
                pre = '0'

            if nu != '0':
                if tmp == 2:
                    answer.append(num[100])
                    answer.append(num[int(nu)])
                else:
                    if tmp == 1 and len(answer) > 0 and pre != '0':
                        n_tmp = answer[-1]
                        answer.pop()
                        if nu == '1':
                            answer.append(num[int(nu)*jari+int(pre)])
                        else:
                            answer.append(num[int(nu)*jari]+'-'+n_tmp)
                    else:
                        answer.append(num[int(nu)*jari])
                pre = nu

        return ' '.join(answer[::-1])

# 다른 사람의 풀이
words = "zero one two three four five six seven eight nine" + \
" ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty" + \
" thirty forty fifty sixty seventy eighty ninety"
words = words.split(" ")
def number2words1(n):
    if n < 20:
        return words[n]
    elif n < 100:
        return words[18 + n // 10] + ('' if n % 10 == 0 else '-' + words[n % 10])
    elif n < 1000:
        return number2words(n // 100) + " hundred" + (' ' + number2words(n % 100) if n % 100 > 0 else '')
    elif n < 1000000:
        return number2words(n // 1000) + " thousand" + (' ' + number2words(n % 1000) if n % 1000 > 0 else '')

if __name__ == '__main__':
    # print(number2words(0), "zero")
    # print(number2words(1), "one")
    # print(number2words(8), "eight")
    # print(number2words(10), "ten")
    # print(number2words(19), "nineteen")
    #print(number2words(20), "twenty")
    print(number2words(22), "twenty-two")
    print(number2words(54), "fifty-four")
    print(number2words(80), "eighty")
    print(number2words(98), "ninety-eight")
    print(number2words(100), "one hundred")
    print(number2words(301), "three hundred one")
    print(number2words(793), "seven hundred ninety-three")
    print(number2words(800), "eight hundred")
    print(number2words(650), "six hundred fifty")
    print(number2words(1000), "one thousand")
    print(number2words(1003), "one thousand three")
    print(number2words(250605))