# 문제
# First non-repeating character
# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

# 나의 풀이
def first_non_repeating_letter(string):
    for s in string:
        if string.lower().count(s.lower()) == 1:
            return s
    return ''

# 다른 사람의 풀이
from collections import Counter
def first_non_repeating_letter1(string):
    cnt = Counter(string.lower())
    for letter in string:
        if cnt[letter.lower()] == 1:
            return letter
    return ''

print(first_non_repeating_letter('a'), 'a')
print(first_non_repeating_letter('stress'), 't')
print(first_non_repeating_letter('moonmen'), 'e')

print(first_non_repeating_letter(''), '')

print(first_non_repeating_letter('abba'), '')
print(first_non_repeating_letter('aa'), '')

print(first_non_repeating_letter('~><#~><'), '#')
print(first_non_repeating_letter('hello world, eh?'), 'w')

print(first_non_repeating_letter('sTreSS'), 'T')
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')