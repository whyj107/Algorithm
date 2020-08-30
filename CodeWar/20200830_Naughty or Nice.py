# 문제
# Naughty or Nice?
# https://www.codewars.com/kata/52a6b34e43c2484ac10000cd/train/python

# 나의 풀이
def get_nice_names(people):
    return [i['name'] for i in people if i['was_nice']]

def get_naughty_names(people):
    return [i['name'] for i in people if not i['was_nice']]

if __name__=='__main__':
    naughty = [{'name': 'xDranik', 'was_nice': False}]
    nice = [{'name': 'Santa', 'was_nice': True}, {'name': 'Warrior reading this kata', 'was_nice': True}]

    print(get_nice_names(naughty), [])
    print(get_nice_names(nice), ['Santa', 'Warrior reading this kata'])
    print(get_naughty_names(naughty), ['xDranik'])
    print(get_naughty_names(nice), [])