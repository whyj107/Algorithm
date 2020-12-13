# Thinking & Testing : Uniq or not Uniq
# https://www.codewars.com/kata/56d949281b5fdc7666000004/train/python

# 나의 풀이
def testit(a, b):
    a = list(set(a))
    b = list(set(b))
    a.extend(b)
    return sorted(a)

# 다른 사람의 풀이
def testit1(a, b):
    return sorted(list(set(a)) + list(set(b)))

print(testit([0],[1]), [0,1])
print(testit([1,2],[3,4]), [1,2,3,4])
print(testit([1],[2,3,4]), [1,2,3,4])
print(testit([1,2,3],[4]), [1,2,3,4])
print(testit([1,2],[1,2]), [1,1,2,2])