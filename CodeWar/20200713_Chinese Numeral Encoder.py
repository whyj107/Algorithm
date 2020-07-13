# 문제
# Chinese Numeral Encoder

# 나의 풀이
def to_chinese_numeral(n):
    numerals = {
        0: "零",
        1: "一",
        2: "二",
        3: "三",
        4: "四",
        5: "五",
        6: "六",
        7: "七",
        8: "八",
        9: "九",
        10: "十",
        100: "百",
        1000: "千",
        10000: "万"
    }
    answer = ""
    original = n
    if n < 0:
        answer += "负"
        n *= -1
        original = n
    elif n == 10:
        answer += numerals[10]
        return answer
    tmp = str(n).split('.')
    for i in reversed(sorted(numerals.keys())):
        while i <= n:
            if original >= 20 and n>=10:
                cnt = int(n // i)
                n %= i
                answer += numerals[cnt]
            else:
                n -= i
            answer += numerals[i]

            if n == 0:
                return answer
            elif 0 < n < 1:
                answer += "点"
                for j in tmp[1]:
                    answer += numerals[int(j)]
                return answer

            if i > 10 and n%i < (i/10) and n%i != 0:
                answer += numerals[0]

# Warriors Code
import re

NEG, DOT, _, *DIGS = "负点 零一二三四五六七八九"
POWS = " 十 百 千 万".split(' ')
NUMS = {str(i):c for i,c in enumerate(DIGS)}
for n in range(10): NUMS[str(n+10)] = POWS[1] + DIGS[n]*bool(n)


def to_chinese_numeral1(n):
    ss = str(abs(n)).split('.')
    return NEG*(n<0) + parse(ss[0]) + (len(ss)>1 and decimals(ss[1]) or '')

def decimals(digs): return DOT + ''.join(NUMS[d] for d in digs)

def parse(s):
    if s in NUMS: return NUMS[s]
    s = ''.join(reversed([ NUMS[d] + POWS[i]*(d!='0') for i,d in enumerate(reversed(s)) ]))
    return re.sub(f'零+$|(?<=零)零+', '', s)

if __name__ == '__main__':
    print(to_chinese_numeral(9) == '九')
    print(to_chinese_numeral(-5) == '负五')
    print(to_chinese_numeral(0.5) == '零点五')
    print(to_chinese_numeral(11) == '十一')
    print(to_chinese_numeral(110) == '一百一十')
    print(to_chinese_numeral(111) == '一百一十一')
    print(to_chinese_numeral(1000) == '一千')
    print(to_chinese_numeral(10000) == '一万')
    print(to_chinese_numeral(10006) == '一万零六')
    print(to_chinese_numeral(10306.005) == '一万零三百零六点零零五')