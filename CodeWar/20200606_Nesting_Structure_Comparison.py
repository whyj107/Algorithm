# 문제
# Nesting Structure Comparison
# Complete the function/method (depending on the language) to return true/True
# when its argument is an array that has the same nesting structure as the first array.

# 입력 == 출력
# Test.assert_equals(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
# Test.assert_equals(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")

# My Code
def same_structure_as(original, other):
    if type(original) != type(other):
        return False
    if type(original) == list and type(other) == list:
        if len(original) != len(other):
            return False
    for i in range(len(original)):
        if type(original[i]) == list:
            tmp = same_structure_as(original[i], other[i])
            if not tmp:
                return False
    return True

# Warriors Code
def same_structure_as1(original, other):
    if type(original) == list == type(other):
        return len(original) == len(other) and all(map(same_structure_as, original, other))
    else:
        return type(original) != list != type(other)

if __name__ == '__main__':
    print(same_structure_as([1, '[', ']'], ['[', ']', 1]))
    print(same_structure_as([1, [1, 1]], [2, [2, 2]]), True)
    print(same_structure_as([1, [1, 1]], [[2, 2], 2]), False)