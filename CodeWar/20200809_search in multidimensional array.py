# 문제
# search in multidimensional array
# https://www.codewars.com/kata/52840d2b27e9c932ff0016ae/train/python

# 나의 풀이
def locate(seq, value):
    if value in seq:
        return True
    for i in seq:
        if type(i) == list:
            if locate(i, value):
                return True
    return False

# 다른 사람의 풀이
def locate1(seq, value):
    for s in seq:
        if s == value or (isinstance(s,list) and locate(s, value)):
            return True
    return False

if __name__ == '__main__':
    print(locate(['a', 'b', ['c', 'd', ['e']]], 'a'), True)
    print(locate(['a', 'b', ['c', 'd', ['e']]], 'd'), True)
    print(locate(['a', 'b', ['c', 'd', ['e']]], 'e'), True)
    print(locate(['a', 'b', ['c', 'd', ['e']]], 'f'), False)
    print(locate(['a', 'b', ['c', 'd', ['e', ['a', 'b', ['c', 'd', ['e4']]]]]], 'e4'), True)