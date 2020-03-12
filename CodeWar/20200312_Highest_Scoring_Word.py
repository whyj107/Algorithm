# 문제
# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

# 입력 == 출력
# test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
# test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
# test.assert_equals(high('take me to semynak'), 'semynak')

# --------------------------
# ord('문자') : 아스키 코드 번호
# a : 97
# z : 122
# 각 아스키 코드에 (- 96) * 단어 길이하면 된다.
# --------------------------

# My Code
def high(x):
    answer_ = []
    sum_ = 0
    for i in x:
        if i is ' ':
            answer_.append(sum_)
            sum_ = 0
            continue
        else:
            sum_ += ord(i)-96
    answer_.append(sum_)
    return x.split()[answer_.index(max(answer_))]

# Warriors Code
def high_(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

if __name__=='__main__':
    answer = high('man i need a taxi up to ubud')
    print(answer)
    answer = high('what time are we climbing up the volcano')
    print(answer)
    answer = high('take me to semynak')
    print(answer)