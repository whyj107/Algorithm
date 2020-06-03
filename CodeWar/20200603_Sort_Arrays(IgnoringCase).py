# 문제
# Sort Arrays (Ignoring Case)
# Sort the given strings in alphabetical order, case insensitive.

# 입력 == 출력
# Test.assert_equals(sortme(["Hello", "there", "I'm", "fine"]), ["fine", "Hello", "I'm", "there"])
# Test.assert_equals(sortme(["C", "d", "a", "B"]), ["a", "B", "C", "d"])
# Test.assert_equals(sortme(["CodeWars"]), ["CodeWars"])

# My Code
def sortme(words):
    return sorted(words, key=lambda x: x.lower())

if __name__ == '__main__':
    print(sortme(["Hello", "there", "I'm", "fine"]), ["fine", "Hello", "I'm", "there"])
    print(sortme(["C", "d", "a", "B"]), ["a", "B", "C", "d"])
    print(sortme(["CodeWars"]), ["CodeWars"])