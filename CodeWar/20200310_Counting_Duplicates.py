# 문제
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
#
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

# 입력 == 출력
# test.assert_equals(duplicate_count("abcde"), 0)
# test.assert_equals(duplicate_count("abcdea"), 1)
# test.assert_equals(duplicate_count("indivisibility"), 1)

# --------------------------
# 문자열 count()
# : 부분문자열의 개수를 세는 메소드
# 문자열.count('개수 세고싶은 문자')

# text.lower() : 문자열 소문자로 변경
# set(text.lower()) : 중복 제거
# --------------------------

# My Code
def duplicate_count(text):
    cnt = 0
    for i in set(text.lower()):
        if text.lower().count(i) > 1:
            cnt += 1
    return cnt

# Warriors Code
def duplicate_count_(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])

if __name__=='__main__':
    answer = duplicate_count("abcde")
    print(answer)
    answer = duplicate_count("aabBcde")
    print(answer)