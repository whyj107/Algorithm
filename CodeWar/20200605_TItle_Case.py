# 문제
# Title Case
# A string is considered to be in title case if each word in the string is either (a) capitalised
# (that is, only the first letter of the word is in upper case)
# or (b) considered to be an exception
# and put entirely into lower case unless it is the first word,
# which is always capitalised.
#
# Write a function that will convert a string into title case, given an optional list of exceptions (minor words).
# The list of minor words will be given as a string with each word separated by a space.
# Your function should ignore the case of the minor words string
# -- it should behave in the same way
# even if the case of the minor word string is changed.

# 입력 == 출력
# Test.assert_equals(title_case(''), '')
# Test.assert_equals(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
# Test.assert_equals(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
# Test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')

def title_case(title, minor_words=''):
    tmp = title.title().split(" ")
    answer = [tmp[0]]
    for i in tmp[1:]:
        tmp_bool = True
        for j in minor_words.split(" "):
            if i.lower() == j.lower():
                answer.append(i.lower())
                tmp_bool = False
        if tmp_bool:
            answer.append(i)
    return ' '.join(answer)

def title_case1(title, minor_words=''):
    title, minor_words = title.lower().split(), minor_words.lower().split()
    for i in range(len(title)):
        if i == 0 or title[i] not in minor_words:
            title[i] = title[i].capitalize()
    return ' '.join(title)

if __name__ == '__main__':
    # print(title_case(''), '')
    print(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
    print(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
    print(title_case('the quick brown fox'), 'The Quick Brown Fox')