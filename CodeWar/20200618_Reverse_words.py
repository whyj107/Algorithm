# 문제
# Reverse words
# Complete the function that accepts a string parameter, and reverses each word in the string.
# All spaces in the string should be retained.

# 입력 == 출력
# test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
# test.assert_equals(reverse_words('apple'), 'elppa')
# test.assert_equals(reverse_words('a b c d'), 'a b c d')
# test.assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')

# My Code
def reverse_words(text):
    return ' '.join([i[::-1] for i in text.split(' ')])

# Warriors Code
# 정규표현식
import re

def reverse_words1(str):
  return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)

if __name__ == '__main__':
    print(reverse_words('The quick brown fox jumps over the lazy dog.'),
                       'ehT kciuq nworb xof spmuj revo eht yzal .god')
    print(reverse_words('apple'), 'elppa')
    print(reverse_words('a b c d'), 'a b c d')
    print(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')