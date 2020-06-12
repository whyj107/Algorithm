# 문제
# The Hashtag Generator
# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
#
# Here's the deal:
#
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

# 입력 == 출력
# Test.assert_equals(generate_hashtag(''), False, 'Expected an empty string to return False')
# Test.assert_equals(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
# Test.assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
# Test.assert_equals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
# Test.assert_equals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
# Test.assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
# Test.assert_equals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
# Test.assert_equals(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
# Test.assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
# Test.assert_equals(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False,
# 'Should return False if the final word is longer than 140 chars.')

# My Code
def generate_hashtag(s):
    if len(s) == 0 or len(s) > 140:
        return False
    return '#' + s.title().replace(' ', '')

if __name__ == '__main__':
    print(generate_hashtag(''), False, 'Expected an empty string to return False')
    print(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
    print(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
    print(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
    print(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
    print(generate_hashtag('codewars is nice'), '#CodewarsIsNice',
                       'Should capitalize first letters of words.')
    print(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice',
                       'Should capitalize all letters of words - all lower case but the first.')
    print(generate_hashtag('c i n'), '#CIN',
                       'Should capitalize first letters of words even when single letters.')
    print(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice',
                       'Should deal with unnecessary middle spaces.')
    print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'),
                       False, 'Should return False if the final word is longer than 140 chars.')