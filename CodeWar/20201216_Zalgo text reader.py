# Zalgo text reader
# https://www.codewars.com/kata/588fe9eaadbbfb44b70001fc/train/python

# 나의 풀이 : 인터넷 서치로 찾아보았다. Zalgo 라는 것을 처음 봤기에...
import unicodedata
def read_zalgo(zalgotext):
    return ''.join([c for c in unicodedata.normalize('NFD', zalgotext) if unicodedata.category(c) not in ['Mn', 'Me']])

# 다른 사람의 풀이 : 그냥 ascii인지 확인하고 그것만 출력해도 상관없었다.
def read_zalgo1(zalgotext):
    return "".join([c for c in zalgotext if c.isascii()])

import re
def read_zalgo2(s):
    return re.sub('[^\w .,!?]', '',s)

print(read_zalgo("H̗̪͇͓̙͎̣̄ͬa͚̯̦͉̖̥v͆ͩ̃͆̓̐ͥe̟͎͖͕͍̎ ̰͚̩̟͕̰͊̽̍ͯ̌͊ā̖̪͉͍̥͙̿ͩ̃ͅ ̬̥͎͑̿ͧg̰̳̺͔̦͉ͫ̀̐̓̐r̝̫̱̘̰͐͋ͯͭͭͭ͆e͙͕̖̗͙̰͌ͭä͓͚̝͓́̌͑ͪ͊ṱͥ ̱ͣd͎͔͎͇̫̪̘̃͐̇à͕̮̈͋ͪy̼̳̱ͮ!̳̥̰̭͇̔ͮ̽̓"), "Have a great day!")
