# Are they the "same"?
# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

# 나의 풀이
def comp(array1, array2):
    if array1 is None or array2 is None or (array1 == [] and array2 != []):
        return False
    for i in array1:
        if i**2 in array2:
            array2.remove(i**2)
        else:
            return False
    return True

# 다른 사람의 풀이
def comp1(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

def comp2(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(a1, a2), True)