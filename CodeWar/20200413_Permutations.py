# 문제
# In this kata you have to create all permutations of an input string and remove duplicates,
# if present. This means, you have to shuffle all letters from the input in all possible orders.

# 입력 == 출력
# Test.assert_equals(sorted(permutations('a')), ['a']);
# Test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
# Test.assert_equals(sorted(permutations('aabb')),
# ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])

# My Code
import itertools
def permutations(string):
    # 순열 만들기
    result = list(itertools.permutations(string, len(string)))

    # [('a', 'b')] -> ['ab']
    result = list(set([''.join(i) for i in result]))

    # 정렬
    result.sort()
    print(result)
    return result

# 한줄로 줄이기
def permutations1(string):
    return list(''.join(p) for p in set(itertools.permutations(string)))

# itertools 안쓰고 작성
def permutations2(string):
    if len(string) == 1: return set(string)
    first = string[0]
    rest = permutations(string[1:])
    result = set()
    for i in range(0, len(string)):
        for p in rest:
            result.add(p[0:i] + first + p[i:])
    return result

if __name__=='__main__':
    asnwer = permutations('a')
    print(asnwer)