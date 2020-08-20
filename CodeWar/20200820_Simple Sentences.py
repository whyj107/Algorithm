# 문제
# Simple Sentences
# https://www.codewars.com/kata/5297bf69649be865e6000922/train/python

# 나의 풀이
def make_sentences(parts):
    l = []
    pre = ''
    for i in parts[::-1]:
        if i.isalpha() or i.isdigit():
            if not (pre.isalpha() or pre.isdigit()):
                l.append(i+pre)
            else:
                l.append(i)
        else:
            if pre == i:
                continue
        pre = i
    answer = ' '.join(l[::-1])
    return answer if answer[-1] == '.' else answer+'.'

# 다른 사람의 풀이
def make_sentences1(parts):
    return ' '.join(parts).replace(' ,', ',').strip(' .') + '.'

if __name__ == "__main__":
    print(make_sentences(['hello', 'world']), 'hello world.')
    print(make_sentences(['Quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']),
                       'Quick brown fox jumped over the lazy dog.')

    print(make_sentences(['hello', ',', 'my', 'dear']), 'hello, my dear.')
    print(make_sentences(['one', ',', 'two', ',', 'three']), 'one, two, three.')
    print(
        make_sentences(['One', ',', 'two', 'two', ',', 'three', 'three', 'three', ',', '4', '4', '4', '4']),
        'One, two two, three three three, 4 4 4 4.')

    print(make_sentences(['hello', 'world', '.']), 'hello world.')
    print(make_sentences(['Bye', '.']), 'Bye.')

    print(make_sentences(['hello', 'world', '.', '.', '.']), 'hello world.')
    print(make_sentences(
        ['The', 'Earth', 'rotates', 'around', 'The', 'Sun', 'in', '365', 'days', ',', 'I', 'know', 'that', '.', '.',
         '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']),
                       'The Earth rotates around The Sun in 365 days, I know that.')
