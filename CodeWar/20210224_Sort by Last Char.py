# Sort by Last Char
# https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0/train/python

# 나의 풀이
def last(s):
    return sorted(s.split(), key=lambda x: x[-1])

# 다른 사람의 풀이
from operator import itemgetter

def last1(s):
    return sorted(s.split(), key=itemgetter(-1))

print(last("man i need a taxi up to ubud"), ["a", "need", "ubud", "i", "taxi", "man", "to", "up"])
print(last("what time are we climbing up the volcano"), ["time", "are", "we", "the", "climbing", "volcano", "up", "what"])
print(last("take me to semynak"), ["take", "me", "semynak", "to"])
print(last("massage yes massage yes massage"), ["massage", "massage", "massage", "yes", "yes"])
print(last("take bintang and a dance please"), ["a", "and", "take", "dance", "please", "bintang"])