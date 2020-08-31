# 문제
# Is Integer Array?
# https://www.codewars.com/kata/52a112d9488f506ae7000b95/train/python

# 나의 풀이
def is_int_array(arr):
    try:
        if not type(arr) == list: return False
        for i in arr:
            if i != int(i):
                return False
    except:
        return False
    return True

# 다른 사람의 풀이
def is_int_array(a):
    return isinstance(a, list) and all(isinstance(x, (int, float)) and x == int(x) for x in a)

if __name__ == '__main__':
    # print(is_int_array([]), True)
    # print(is_int_array([1, 2, 3, 4]), True)
    # print(is_int_array([-11, -12, -13, -14]), True)
    # print(is_int_array([1.0, 2.0, 3.0]), True)
    # print(is_int_array([1, 2, None]), False)
    # print(is_int_array(None), False)
    print(is_int_array(""), False)
    # print(is_int_array([None]), False)
    # print(is_int_array([1.0, 2.0, 3.0001]), False)
    # print(is_int_array(["-1"]), False)