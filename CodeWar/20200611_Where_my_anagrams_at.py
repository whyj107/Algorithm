# 문제
# Where my anagrams at?
# What is an anagram? Well, two words are anagrams of each other
# if they both contain the same letters.

# 입력 == 출력
# Test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
# Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])

# My Code
from collections import Counter
def anagrams(word, words):
    return [i for i in words if Counter(word) == Counter(i) ]

# Warriors Code
def anagrams1(word, words):
    return [item for item in words if sorted(item)==sorted(word)]

if __name__ == '__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
