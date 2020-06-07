# 문제
# Return substring instance count - 2
# Complete the solution so that it
# returns the number of times the search_text is found within the full_text.

# 입력 == 출력
# Test.assert_equals(search_substr('aa_bb_cc_dd_bb_e', 'bb'), 2)
# Test.assert_equals(search_substr('aaabbbcccc', 'bbb'), 1)
# Test.assert_equals(search_substr('aaacccbbbcccc', 'cc'), 5)
# Test.assert_equals(search_substr('aaa', 'aa'), 2)
# Test.assert_equals(search_substr('aaa', 'aa',False), 1)
# Test.assert_equals(search_substr('aaabbbaaa', 'bb',False), 1)
# Test.assert_equals(search_substr('a', ''), 0)
# Test.assert_equals(search_substr('', 'a'), 0)
# Test.assert_equals(search_substr('', ''), 0)
# Test.assert_equals(search_substr('', '',False), 0)

# My Code
def search_substr(full_text, search_text, allow_overlap=True):
    if search_text == '':
        return 0
    if not allow_overlap:
        return full_text.count(search_text)
    else:
        cnt = 0
        while full_text.find(search_text) != -1:
            idx = full_text.find(search_text) + 1
            full_text = full_text[idx:]
            cnt += 1
        return cnt

# Warriors Code
import re
def search_substr1(full_text, search_text, allow_overlap=True):
    if not full_text or not search_text: return 0
    return len(re.findall(f'(?=({search_text}))' if allow_overlap else search_text, full_text))

if __name__ == '__main__':
    print(search_substr('aa_bb_cc_dd_bb_e', 'bb'), 2)
    print(search_substr('aaabbbcccc', 'bbb'), 1)
    print(search_substr('aaacccbbbcccc', 'cc'), 5)
    print(search_substr('aaa', 'aa'), 2)
    print(search_substr('aaa', 'aa', False), 1)
    print(search_substr('aaabbbaaa', 'bb', False), 1)
    print(search_substr('a', ''), 0)
    print(search_substr('', 'a'), 0)
    print(search_substr('', ''),  0)
    print(search_substr('', '', False), 0)
