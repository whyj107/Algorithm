# 문제
# Who likes it?
# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.
#
# Implement a function likes :: [String] -> String, which must take in input array,
# containing the names of people who like an item.

# 입력 == 출력
# Test.assert_equals(likes([]), 'no one likes this')
# Test.assert_equals(likes(['Peter']), 'Peter likes this')
# Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
# Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
# Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

# My Code
def likes(names=['no one']):
    if len(names) <= 0:
        return 'no one likes this'
    elif len(names) == 1:
        return ' '.join([names[0], 'likes this'])
    elif len(names) in [2, 3]:
        return ' '.join([', '.join(names[:-1]), 'and', names[-1], 'like this'])
    else:
        return ' '.join([', '.join(names[:2]), 'and', str(len(names)-2),'others like this'])

# Warriors Code
def likes1(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

if __name__ == '__main__':
    print(likes([]) == 'no one likes this')
    print(likes(['Peter']) == 'Peter likes this')
    print(likes(['Jacob', 'Alex']) =='Jacob and Alex like this')
    print(likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this')
    print(likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this')