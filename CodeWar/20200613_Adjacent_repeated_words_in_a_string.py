# 문제
# Adjacent repeated words in a string
# You know how sometimes you write the the same word twice in a sentence,
# but then don't notice that it happened?
# For example, you've been distracted for a second.
# Did you notice that *"the"* is doubled in the first sentence of this description?
#
# As as aS you can see, it's not easy to spot those errors,
# especially if words differ in case, like *"as"* at the beginning of the sentence.
#
# Write a function that counts the number of sections repeating the same word (case insensitive).
# The occurence of two or more equal words next after each other count as one.

# 입력 == 출력
# test.assert_equals(count_adjacent_pairs(''), 0)
# test.assert_equals(count_adjacent_pairs('orange Orange kiwi pineapple apple'), 1)
# test.assert_equals(count_adjacent_pairs('banana banana banana'), 1)
# test.assert_equals(count_adjacent_pairs('banana banana banana terracotta banana terracotta terracotta pie!'), 2)
# test.assert_equals(count_adjacent_pairs('pineapple apple'), 0)

# My Code
def count_adjacent_pairs(st):
    answer = 0
    tmp = True
    pre = ''
    for i in st.split(' '):
        if i != '':
            if pre == i.lower():
                if tmp:
                    tmp = False
                    answer += 1
            else:
                tmp = True
        pre = i.lower()
    return answer

from itertools import groupby
def count_adjacent_pairs1(st):
    return len([name for name,group in groupby(st.lower().split(' ')) if len(list(group))>=2])

if __name__ == '__main__':
    print(count_adjacent_pairs('objECT ObjeCt objECT dict dIct dElaTtr SET Set Filter IMPORt gEtAttr GetATTR GEtatTR Bin BiN biN BiN booL Bool booL booL'), 6)
    print(count_adjacent_pairs('orange Orange kiwi pineapple apple'), 1)
    print(count_adjacent_pairs('banana banana banana'), 1)
    print(count_adjacent_pairs('banana banana banana terracotta banana terracotta terracotta pie!'), 2)
    print(count_adjacent_pairs('pineapple     apple'), 0)