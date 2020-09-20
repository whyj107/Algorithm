# 문제
# WeIrD StRiNg CaSe
# https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python

# 나의 풀이
def to_weird_case(string):
    answer = []
    for s in string.split(' '):
        tmp = ""
        for idx, i in enumerate(s):
            if idx%2 == 0: tmp += i.upper()
            else: tmp += i.lower()
        answer.append(tmp)
    return ' '.join(answer)

# 다른 사람의 풀이
def to_weird_case_word(string):
    return "".join(c.upper() if i % 2 == 0 else c for i, c in enumerate(string.lower()))

def to_weird_case1(string):
    return " ".join(to_weird_case_word(str) for str in string.split())

print(to_weird_case('This'), 'ThIs')
print(to_weird_case('is'), 'Is')
print(to_weird_case('This is a test'), 'ThIs Is A TeSt')
