# Coding Meetup #5 - Higher-Order Functions Series - Prepare the count of languages
# https://www.codewars.com/kata/5828713ed04efde70e000346/train/python

# 나의 풀이
def count_languages(lst):
    dict = {}
    for l in lst:
        if l['language'] in dict.keys():
            dict[l['language']] += 1
        else:
            dict[l['language']] = 1
    return dict

# 다른 사람의 풀이
from collections import Counter
def count_languages1(lst):
    return Counter([d['language'] for d in lst])

list1 = [{'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19,
          'language': 'C'},
         {'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
         {'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
         {'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
        ]

answer = {'C': 2, 'JavaScript': 1, 'Ruby': 1 }
print(count_languages(list1), answer);