# 문제
# Format words into a sentence
# Complete the method so that it formats the words into a single comma separated value.
# The last word should be separated by the word 'and' instead of a comma.
# The method takes in an array of strings and returns a single formatted string.
# Empty string values should be ignored.
# Empty arrays or null/nil values being passed into the method should result in an empty string being returned.

# 입력 == 출력
# Test.assert_equals(format_words(['one', 'two', 'three', 'four']), 'one, two, three and four', "formatWords(['one', 'two', 'three', 'four'] should return 'one, two, three and four'")
# Test.assert_equals(format_words(['one']), 'one', "formatWords(['one']) should return 'one'")
# Test.assert_equals(format_words(['one', '', 'three']), 'one and three', "formatWords(['one', '', 'three']) should return 'one and three'")
# Test.assert_equals(format_words(['', '', 'three']), 'three', "formatWords(['', '', 'three']) should return 'three'")
# Test.assert_equals(format_words(['one', 'two', '']), 'one and two', "formatWords(['one', 'two', '']) should return 'one and two'")
# Test.assert_equals(format_words([]), '', 'formatWords([]) should return ""')
# Test.assert_equals(format_words(None), '', 'formatWords(null) should return ""')
# Test.assert_equals(format_words(['']), '', 'formatWords([""]) should return ""')

# My Code
def format_words(words):
    answer = []
    try:
        for i in words:
            if len(i) > 0:
                answer.append(i)
        return ', '.join(answer[:-1]) + ' and ' + answer[-1] if len(answer) > 1 else answer[0]
    except:
        return ''
    
if __name__ == '__main__':
    print(format_words(['one', 'two', 'three', 'four']))
    print(format_words(['one']))
    print(format_words(['one', '', 'three']))
    print(format_words(['', '', 'three']))
    print(format_words(['one', 'two', '']))
    print(format_words([]))
    print(format_words(None))
    print(format_words(['']))