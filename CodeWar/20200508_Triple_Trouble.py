# 문제
# Create a function that will return a string
# that combines all of the letters of the three inputed strings in groups.
# Taking the first letter of all of the inputs and grouping them next to each other.
# Do this for every letter, see example below!
#
# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"
#
# Note: You can expect all of the inputs to be the same length.

# 입력 == 출력
# Test.describe("Basic tests")
# Test.assert_equals(triple_trouble("aaa","bbb","ccc"), "abcabcabc")
# Test.assert_equals(triple_trouble("aaaaaa","bbbbbb","cccccc"), "abcabcabcabcabcabc")
# Test.assert_equals(triple_trouble("burn", "reds", "roll"), "brrueordlnsl")
# Test.assert_equals(triple_trouble("Bm", "aa", "tn"), "Batman")
# Test.assert_equals(triple_trouble("LLh", "euo", "xtr"), "LexLuthor")

# My Code
def triple_trouble(one, two, three):
    # 반환 할 변수 생성
    answer = ''
    # for문을 이용하여 각 자릿수를 변수에 더하기
    for i in range(len(one)):
        answer += (one[i] + two[i] + three[i])
    # 정답 반환
    return answer

    # 다른 방법
    return "".join([one[i] + two[i] + three[i] for i in range(len(one))])

if __name__=='__main__':
    print(triple_trouble("aaa", "bbb", "ccc"))
    print(triple_trouble("aaaaaa", "bbbbbb", "cccccc"))
    print(triple_trouble("burn", "reds", "roll"))
    print(triple_trouble("Bm", "aa", "tn"))
    print(triple_trouble("LLh", "euo", "xtr"))