# 문제
# Anagram Detection
# https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python

# 나의 풀이
def is_anagram(test, original):
    return sorted(test.lower())==sorted(original.lower())

if __name__ == '__main__':
    print(is_anagram('Creative', 'Reactive'), True)
    print(is_anagram("foefet", "toffee"), True)
    print(is_anagram("Buckethead", "DeathCubeK"), True)
    print(is_anagram("Twoo", "WooT"), True)
    print(is_anagram("dumble", "bumble"), False)
    print(is_anagram("ound", "round"), False)
    print(is_anagram("apple", "pale"), False)