# 문제
# This time no story, no theory.
# The examples below show you how to write function accum:
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

# 입력 == 출력
# Test.assert_equals(accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
# Test.assert_equals(accum("NyffsGeyylB"), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
# Test.assert_equals(accum("MjtkuBovqrU"), "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
#Test.assert_equals(accum("EvidjUnokmM"), "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
# Test.assert_equals(accum("HbideVbxncC"), "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")

# --------------------------
# 문자열을 대문자로 바꾸는 메소드
# string.upper() : 주어진 문자열에서 모든 알파벳들을 대문자로 변환시킨다.
# string.capitalize() : 주어진 문자열에서 맨 첫 글자를 대문자로 변환시킨다.
# string.title() : 주어진 문자열에서 알파벳 외의 문자(숫자, 특수기호, 띄어쓰기 등)로
#                  나누어져 있는 영단어들의 첫 글자를 모두 대문자로 변환시킨다.
# string.lower() : 주어진 문자열에서 모든 알파벳들을 소문자로 변환시킨다.
# --------------------------

# My Code
def accum(s):
    cnt = 0
    answer = ""
    for i in s:
        cnt += 1
        answer += i*cnt+'-'

    return answer[:-1].title()

# Warriors Code
def accum_(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

if __name__=='__main__':
    s = accum('abcd')
    print(s)
    s = accum('RqaEzty')
    print(s)