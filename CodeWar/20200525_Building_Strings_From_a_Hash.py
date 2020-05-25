# 문제
# Building Strings From a Hash
# Complete the solution so that it takes the object (JavaScript/CoffeeScript) or hash (ruby) passed in
# and generates a human readable string from its key/value pairs.
#
# The format should be "KEY = VALUE".
# Each key/value pair should be separated by a comma except for the last pair.

# 입력 == 출력
# Test.assert_equals(solution({'a': 1, 'b': 2}), 'a = 1,b = 2')
# Test.assert_equals(solution({'a': 'b', 'b': 'a'}), 'a = b,b = a')
# Test.assert_equals(solution({0: 'a', 'b': 2}), '0 = a,b = 2')
# Test.assert_equals(solution({'b': 1, 'c': 2, 'e': 3}), 'b = 1,c = 2,e = 3')
# Test.assert_equals(solution({}), '')

# My Code
def solution(pairs):
    pairs = {str(k):str(pairs[k]) for k in pairs.keys()}
    return ','.join([str(key) + ' = ' + str(pairs[key]) for key in sorted(pairs.keys())])

def solution1(pairs):
    return ','.join(sorted('{} = {}'.format(k, pairs[k]) for k in pairs))

if __name__ == '__main__':
    print(solution({'a': 1, 'b': 2}), 'a = 1,b = 2')
    print(solution({'a': 'b', 'b': 'a'}), 'a = b,b = a')
    print(solution({0: 'a', 'b': 2}), '0 = a,b = 2')
    print(solution({'b': 1, 'c': 2, 'e': 3}), 'b = 1,c = 2,e = 3')
    print(solution({}), '')