# 문제
# Readability is King
# https://www.codewars.com/kata/52b2cf1386b31630870005d4/train/python

# 나의 풀이
def flesch_kincaid(text):
    tt = ['.', '!', '?']
    for i in tt:
        if i in text:
            text = text.replace(i, '.')
    a, b = [], []
    sentence = [t for t in text.split('.') if not t == '']
    sentence1 = []
    for t in sentence:
        tmp = [t1 for t1 in t.split(' ')]
        if '' in tmp: tmp.remove('')
        a.append(len(tmp))
        sentence1 += tmp
    for t in sentence1:
        if t == '':
            continue
        cnt, pre = 0, False
        for i in t:
            if i.lower() in ['a', 'e', 'i', 'o', 'u'] and pre is False:
                pre = True
                cnt += 1
            else:
                pre = False
        b.append(cnt)
    answer = 0.39*(sum(a)/len(a))+11.8*(sum(b)/len(b))-15.59
    return round(answer, 2)

# 다른 사람의 풀이
from re import compile as reCompile
SENTENCE = reCompile(r'[.!?]')
SYLLABLE = reCompile(r'(?i)[aeiou]+')
def count(string, pattern):
    return len(pattern.findall(string))
def flesch_kincaid1(text):
    nWords = text.count(' ') + 1
    return round(0.39 * nWords / count(text, SENTENCE) + 11.8 * count(text, SYLLABLE) / nWords - 15.59, 2)

# print(flesch_kincaid("The turtle is leaving."), 3.67)
# print(flesch_kincaid("A good book is hard to find."), -1.06)
# print(flesch_kincaid("To be or not to be. That is the question."), -0.66)
print(flesch_kincaid("Oh no! The lemming is falling."), 1.31)