# 문제
# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

# 입력 == 출력
# test.describe("Basic Tests")
# test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
# test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
# test.assert_equals(find_short("lets talk about javascript the best language"), 3)
# test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
# test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)

# --------------------------
# 가장 짧은 단어의 길이를 반환하라.
# 코드 길이를 짧게 만들도록 노력해봐야겠다.
# --------------------------

# My Code
def find_short(s):
    l = []
    tmp = s.split()
    for r in tmp:
        l.append(len(r))
    return min(l)

# Warriors Code
def find_short_(s):
    return min(len(x) for x in s.split())

if __name__=='__main__':
    l = find_short("i want to travel the world writing code one day")
    print(l)